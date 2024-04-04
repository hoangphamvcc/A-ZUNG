from full_task.kafka_con_pro import KafkaUtility
from full_task.mongo_querry import mongoQuerry


def queue_scan():
    client = mongoQuerry()
    kafka_worker = KafkaUtility()

    num_channel = int(client.status_find('users')['channel']) + 1
    #print(client.status_find('users'), type(client.status_find('users')), num_channel)
    for channel in range(0, num_channel):
        client.update_set('users', query={'_id': f'{channel}'}, value={'News_count': '0'})
        #client.update_set('News', query={'_id': '0'}, value={'curr_id': '0'})
        client.scan_find(collection='queue_news', query={'user_id': f'{channel}'})
        # kafka_worker.producer_send('send_news',)
        print(client.scan_find(collection='queue_news', query={'user_id': f'{channel}'}))


#queue_scan()
