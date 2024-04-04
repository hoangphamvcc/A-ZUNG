from full_task.mongo_querry import mongoQuerry
from full_task.kafka_con_pro import KafkaUtility
import full_task.kafka_con_pro as kk

client = mongoQuerry()
kafka_worker = KafkaUtility()


def count_event(user_id: int):
    return client.scan_find('users', query={'_id': f'{user_id}'})['News_count']


consumer = kafka_worker.consumer('event_news')     # nhan du lieu tu bang event_news
for msg in consumer:
    print(kk.tranform_msg(msg), type(kk.tranform_msg(msg)))
    # set up cac gia tri data, id tin, id nguoi nhan
    data = kk.tranform_msg(msg)
    user_id = int(kk.tranform_msg(msg)['user_id']) + 1
    news_id = kk.tranform_msg(msg)['news_id']
    count_event_main = int(count_event(user_id))

    if count_event_main < 4:        # tao dieu kien kiem tra, co pass so luong gioi han hay khong
#        news_data = client.scan_find(collection='queue_news', query={})
#"""        if news_data is None:"""
        # send to api
        kafka_worker.producer_send('api_news', data)             # tra du lieu ve topic api
        print('pull api')
#        else:
#            client.insert_one(collection='queue_news', document=data)
#            print('queue load')
    else:                          # neu vuot qua so luong, tra ket qua ve bang queue
        print('full news')
        client.insert_one(collection='queue_news', document=data)

"""     """
