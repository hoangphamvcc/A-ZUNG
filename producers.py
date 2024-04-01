from kafka import KafkaProducer
import json
import time
from rss_collector import Rss_Coll


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['10.5.69.117:9092'],  # server name
    value_serializer=json_serializer,  # function callable
    # partitioner = get_partitioner, # function return 0 >>> only partition_0 can received messages
)


def do_procerduce() -> None:
    a = Rss_Coll()
    a1 = a.time_index()
    for i in a1:
        producer.send('test123', {'Title': '{}'.format(i['Title']),
                                  'Link': '{}'.format(i['Link']),
                                  'Date': '{}'.format(i['Date']),
                                  'Image': '{}'.format(i['Image'])})
        print(i)
        time.sleep(5)


if __name__ == '__main__':
    while True:
        do_procerduce()
