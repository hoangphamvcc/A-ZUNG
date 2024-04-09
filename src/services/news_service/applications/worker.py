from datetime import datetime

from src.services.news_service.handlers import VNExpressRSSHandler, HourlyNewsPublishHandler
from src.services.news_service.repositories import (VNExpressRecentRSSRepository, MongoNewsRepository,
                                                    MongoHourlyNewsRepository,
                                                    KafkaNewsPublishSender)


def send_event():
    current_time = datetime.now()
    handler = HourlyNewsPublishHandler(MongoHourlyNewsRepository(), KafkaNewsPublishSender())
    handler.handle(current_time)


def worker():
    # co tin dong dat, gui tin hourly
    send_event()
