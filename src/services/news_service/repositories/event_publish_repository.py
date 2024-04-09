import json
import os
from datetime import datetime

import kafka

from src.services.news_service.domains import News
from src.services.news_service.handlers import NewsPublishSender

NEWS_TOPIC = os.getenv("NEWS_TOPIC")
NEWS_BOOTSTRAP_SERVERS = os.getenv("NEWS_BOOTSTRAP_SERVERS")


class KafkaNewsPublishSender(NewsPublishSender):
    def __init__(self):
        self.__producer = kafka.KafkaProducer(bootstrap_servers=NEWS_BOOTSTRAP_SERVERS,
                                              value_serializer=KafkaNewsPublishSender.json_serializer)

    @staticmethod
    def json_serializer(data: dict):
        # convert datetime to string ISO
        for key, value in data['payload'].items():
            if isinstance(value, datetime):
                data['payload'][key] = value.isoformat()

        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()

        return json.dumps(data).encode('utf-8')

    def send(self, news: News) -> bool:
        self.__producer.send(NEWS_TOPIC, news.to_publishable_news().to_dict())
        return True
