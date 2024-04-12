from flask import Flask
from db import Connection
from flask_restful import Resource, Api
from uuid import uuid1
from flask import request, jsonify
from src.common import datetimestr_to_datetime
from bson import ObjectId

app = Flask(__name__)
db = Connection('task')


def page_limit(page: int, limit: int) -> tuple:
    limit_end = limit * page
    limit_start = limit * (page - 1)
    return limit_end, limit_start


@app.route('/')
def index():
    return 'Hello'


@app.route('/api/user/<string:name>', methods=['GET'])
def get_user(name):
    demo_data = {'name': name,
                 'data': {'item': [],
                          'meta': {'page_count': 0,
                                   'page': 0}
                          }
                 }
    datetime_str = request.args.get('datetime_str')
    limit = request.args.get('limit')
    page = request.args.get('page')
    if datetime_str and limit:
        start_hour = datetimestr_to_datetime(datetime_str)
        end_hour = start_hour.replace(hour=start_hour.hour + 1)
        payload = {'received_at': {'$gt': start_hour, '$lt': end_hour}}
        # insert meta data
        demo_data['data']['meta']['total_count'] = db['received_news_collection'].count_documents(payload)
        demo_data['data']['meta']['page'] = int(page)
        demo_data['data']['meta']['page_count'] = int(int(demo_data['data']['meta']['total_count']) / int(page))
        # demo_data['limit'] = limit
        # querry
        limit_end, limit_start = page_limit(int(page), int(limit))
        for index, item in enumerate(db['received_news_collection'].find(payload).sort('received_at', -1).limit(limit_end)):
            if index >= limit_start:
                # change format of _id and received_at to isoformat
                item['_id'] = str(item['_id'])
                item['received_at'] = item['received_at'].astimezone().isoformat()
                demo_data['data']['item'].append(item)
    return jsonify(demo_data), 200


if __name__ == "__main__":
    app.run(port=8889, debug=False)
    # print(type(next(db['received_news_collection'].find())))
