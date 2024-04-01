from kafka import KafkaProducer
import json
import time
import pymongo


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['10.5.69.117:9092'],  # server name
    value_serializer=json_serializer,  # function callable
    # partitioner = get_partitioner, # function return 0 >>> only partition_0 can received messages
)

client = pymongo.MongoClient("mongodb://10.0.67.162:27017/")

mydb = client['dev1']
event_collect = mydb['event']

if __name__ == '__main__':
    status_document = next(event_collect.find({'_id': '0'}))
    last_collect = int(status_document['last-collect'])
    event_list = event_collect.find({'_id': {'$gt': '{}'.format(last_collect)}})
    for event in event_list:
        producer.send('test-micro', event, partition=0)
        print(event)
        time.sleep(0.3)


