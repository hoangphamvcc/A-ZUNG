import random
from full_task.mongo_querry import mongoQuerry
from full_task.kafka_con_pro import KafkaUtility
import full_task.kafka_con_pro as kk


def generate_event():
    client = mongoQuerry()
    curr_id = int(client.status_find('News')['curr_id'])            # tin cap nhat
    curr_id_rss = int(client.status_find('News')['curr_id_rss'])        # tin moi nhat
    count_user = int(client.status_find('users')['channel'])    # so luong user

    kafka_worker = KafkaUtility()

    for id in range(curr_id, curr_id_rss + 1): # curr_id
        for user in range(0, count_user + 1):
            send_even = random.randrange(0, 3)
            if send_even == 0:
                kafka_worker.producer_send('event_news', {'news_id': f'{id}', 'user_id': f'{user}'}) # gui ket qua den bang event News
                print({'news_id': f'{id}', 'user_id': f'{user}'})
    client.update_set(collection='News', query={'_id': '0'}, value={'curr_id': f'{curr_id_rss}'})     # tra ve gia tri ket qua cap nhat moi nhat
