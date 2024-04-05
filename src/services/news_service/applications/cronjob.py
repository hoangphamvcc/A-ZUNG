import time
from datetime import datetime

import schedule

from src.services.news_service.handlers import VNExpressRSSHandler, HourlyNewsPublishHandler
from src.services.news_service.repositories import (VNExpressRecentRSSRepository, MemoryNewsRepository,
                                                    MongoHourlyNewsRepository,
                                                    KafkaNewsPublishSender)


def request_recent_vn_express_news():
    # Your code here
    handler = VNExpressRSSHandler(VNExpressRecentRSSRepository(), MemoryNewsRepository())
    handler.handle()


def send_news_hourly():
    current_time = datetime.now()
    handler = HourlyNewsPublishHandler(MongoHourlyNewsRepository(), KafkaNewsPublishSender())
    handler.handle(current_time)


def run_cronjob():
    schedule.every(10).seconds.do(request_recent_vn_express_news)
    schedule.every().hour.do(send_news_hourly)
    while True:
        schedule.run_pending()
        time.sleep(1)
