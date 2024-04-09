import os

import kafka

from src.services.news_service.domains import News
from src.services.news_service.handlers import NewsPublishSender

NEWS_TOPIC = os.getenv("NEWS_TOPIC")
NEWS_BOOTSTRAP_SERVER = os.getenv("NEWS_BOOTSTRAP_SERVER")


class KafkaNewsPublishSender(NewsPublishSender):
    def __init__(self):
        self.__producer = kafka.KafkaProducer(bootstrap_servers=NEWS_BOOTSTRAP_SERVER)

    def send(self, news: News) -> bool:
        self.__producer.send(NEWS_TOPIC, news.to_publishable_news().to_dict())
        return True
