import time

import schedule

from src.services.news_service.handlers import VNExpressRSSHandler
from src.services.news_service.repositories import VNExpressRecentRSSRepository, MongoNewsRepository


def request_recent_vn_express_news():
    # Your code here
    handler = VNExpressRSSHandler(VNExpressRecentRSSRepository(), MongoNewsRepository())
    handler.handle()


def run_cronjob():
    schedule.every(10).seconds.do(request_recent_vn_express_news)
    while True:
        schedule.run_pending()
        time.sleep(1)
