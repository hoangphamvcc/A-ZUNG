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
    a = next(event_collect.find({'_id': '0'}))
    a1 = int(a['last-collect'])
    b = event_collect.find({'_id': {'$gt': '{}'.format(a1)}})
    for i in b:
        producer.send('test-micro', i, partition=0)
        print(i)
        time.sleep(0.3)


