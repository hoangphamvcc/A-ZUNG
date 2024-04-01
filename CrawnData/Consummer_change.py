from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from Telegram_bot_send import Bot_send
import json
import pymongo

topic = 'test-micro'
consumer = KafkaConsumer(
                         bootstrap_servers='10.5.69.117:9092',
                         )
client = pymongo.MongoClient("mongodb://10.0.67.162:27017/")

mydb = client['dev1']
event_collect = mydb['event']


def update_even(id):
    myquerry = {'_id': '0'}
    newvalues = {'$set': {'last-collect': '{}'.format(id)}}
    event_collect.update_one(myquerry, newvalues)


if __name__ == '__main__':
    consumer.assign([TopicPartition(topic, 1)])
    for msg in consumer:
        msg1 = json.loads(msg.value.decode('utf-8'))
        print(msg1['Send_Event_id'],type(msg1['Send_Event_id']))
        update_even(int(msg1['Send_Event_id']))

