from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
import time


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


def tranform_msg(msg: str):
    return json.loads(msg.value.decode('utf-8'))


class KafkaUtility(object):

    def __init__(self):
        self.bootstrap_servers_producer = ['10.5.69.117:9092']
        self.bootstrap_servers_consumer = '10.5.69.117:9092'
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers_producer,  # server name
            value_serializer=json_serializer,  # function callable
        )

    def producer_send(self, topic: str, msg: dict) -> None:
        self.producer.send(topic, msg)

    def consumer(self, topic):
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=self.bootstrap_servers_consumer,
                                 )
        return consumer

    def consumer_test(self, topic):
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=self.bootstrap_servers_consumer, auto_offset_reset='earliest'
                                 )
        return consumer
