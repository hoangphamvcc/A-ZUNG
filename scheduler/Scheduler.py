import time

import schedule
from full_task.crawl_data.rss_collect import RssColl
from full_task.mongo_querry import mongoQuerry
from full_task.crawl_data.gen_event import generate_event
from full_task.user_check.reset_queue import queue_scan
import requests


def task_RssCollect():
    try:
        data_collect_rss = RssColl().time_index()
        if RssColl().url.status_code in [200, 404]:
            return data_collect_rss
    except:
        pass
    finally:
        client = mongoQuerry()
        for data in data_collect_rss:
            query = {'Rss_id': '{}'.format(data['Rss_id']), 'Time_stamp': '{}'.format(data['Time_stamp'])}
            if client.scan_find(collection='News', query=query) is None:
                curr_id_rss = client.status_find('News')['curr_id_rss']
                # change id
                curr_id_rss = int(curr_id_rss)
                curr_id_rss = str(curr_id_rss + 1)
                data.update({'_id': f'{curr_id_rss}'})
                # add news to news collection
                client.insert_one(collection='News', document=data)
                client.update_set(collection='News', query={'_id': '0'}, value={'curr_id_rss': f'{curr_id_rss}'})
            else:
                pass
            time.sleep(0.1)
            print('success collect')


"""        for x in client.find_all(collection='News'):
            print(x)"""




# crawl_data
schedule.every(10).seconds.do(task_RssCollect)
schedule.every(30).seconds.do(generate_event)
schedule.every(30).seconds.do(queue_scan)
# user_check

#
if __name__ == '__main__':
    while True:
        """try:"""
        schedule.run_pending()
        time.sleep(3)
