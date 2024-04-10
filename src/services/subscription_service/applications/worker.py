import json
import os
import kafka
from src.services.subscription_service.repositories import MongoPublishingNewsRepository, MongoDB, TelegramPublishClient
from src.services.subscription_service.handlers import PublishingNewsHandler, PublishingNewsCommand

NEWS_TOPIC = os.getenv("NEWS_TOPIC")
NEWS_BOOTSTRAP_SERVERS = os.getenv("NEWS_BOOTSTRAP_SERVERS")


# co tin dong dat, gui tin hourly
class Worker:
    def __init__(self):
        self.__consumer = kafka.KafkaConsumer(NEWS_TOPIC, bootstrap_servers=NEWS_BOOTSTRAP_SERVERS,)

    @staticmethod
    def transform(msg: str):
        a = json.loads(msg.value.decode('utf-8'))
        return PublishingNewsCommand(url=a["payload"]['url'],
                                     header=a["payload"]["header"],
                                     published_at=a["payload"]["published_at"],
                                     issued_at=a["issued_at"])

    def worker_run(self):
        for msg in self.__consumer:
            (PublishingNewsHandler(MongoPublishingNewsRepository(MongoDB()),
                                   TelegramPublishClient())
             .handle(self.transform(msg)))
