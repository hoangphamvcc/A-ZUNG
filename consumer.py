from kafka import KafkaConsumer
from Telegram_bot_send import Bot_send
import json


def tranform(msg: str) -> str:
    a = json.loads(msg.value.decode('utf-8'))
    """a khi nay se co 3 truong Title Link Date"""
    send_msg = '*{}*\n_{}_\n{}\n{}'.format(a['Title'], a['Date'], a['Link'], a['Image'])

    return send_msg


topic = 'test123'

if __name__ == '__main__':
    consumer = KafkaConsumer(topic,
                             bootstrap_servers='10.5.69.117:9092',
                             )

    for msg in consumer:
        a = Bot_send(tranform(msg))
        a.send()
        print(tranform(msg))
