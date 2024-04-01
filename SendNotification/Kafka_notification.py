from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from kafka import KafkaProducer
from Telegram_bot_send import Bot_send
import json

topic = 'test-micro'

consumer = KafkaConsumer(
    bootstrap_servers='10.5.69.117:9092',
)


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['10.5.69.117:9092'],  # server name
    value_serializer=json_serializer,  # function callable
    # partitioner = get_partitioner, # function return 0 >>> only partition_0 can received messages
)

if __name__ == '__main__':
    consumer.assign([TopicPartition(topic, 0)])
    for msg in consumer:
        msg1 = json.loads(msg.value.decode('utf-8'))
        #a = Bot_send(msg1)
        #a.send()
        print(msg1['_id'])
        producer.send('test-micro', {'Send_Event_id': msg1['_id']}, partition=1)
        #a = Bot_send({'Send_Event_id': msg1['_id']})
        #a.send()

