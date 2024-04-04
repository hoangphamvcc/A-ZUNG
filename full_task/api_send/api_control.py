from full_task.mongo_querry import mongoQuerry
from full_task.kafka_con_pro import KafkaUtility
import full_task.kafka_con_pro as kk
import datetime
from full_task.Telegram_bot_send import Bot_send


def count_event(user_id):
    return client.scan_find('users', query={'_id': f'{user_id}'})['News_count']


client = mongoQuerry()
kafka_worker = KafkaUtility()

consumer = kafka_worker.consumer('api_news')  # hub du lieu tu topic api
for msg in consumer:
    # update data;  doc data tu topic api, tra ve cac ket qua can thiet
    user_id = int(kk.tranform_msg(msg)['user_id']) + 1
    news_id = kk.tranform_msg(msg)['news_id']
    news_data = client.scan_find(collection='News', query={'_id': f'{news_id}'})
    news_data.update({'Publish time': f'{datetime.datetime.now()}','user_id': '{}'.format(kk.tranform_msg(msg)['user_id'])})
    # send event
    print(news_data)
    if user_id == 1:    # gui du lieu den tele, cap nhat du lieu count
        tele_client = Bot_send(news_data)
        tele_client.send()
        # cap nhat last_id, count
        client.update_set(collection='users', query={'_id': f'{user_id}'}, value={'last_event_id': f'{news_id}'})
        client.update_set(collection='users', query={'_id': f'{user_id}'}, value={'News_count': '{}'.format(int(count_event(user_id))+1)})
