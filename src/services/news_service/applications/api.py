from datetime import datetime

from src.services.news_service.handlers import VNExpressRSSHandler, HourlyNewsPublishHandler
from src.services.news_service.repositories import (VNExpressRecentRSSRepository, MongoNewsRepository,
                                                    MongoHourlyNewsRepository,
                                                    KafkaNewsPublishSender)


def api():
    handler = VNExpressRSSHandler(VNExpressRecentRSSRepository(), MongoNewsRepository())
    saved_items = handler.handle()
    return {
        'message': 'success',
        'data': saved_items
    }, 200


def api_send_news_manually():
    current_time = datetime.now()
    handler = HourlyNewsPublishHandler(MongoHourlyNewsRepository(), KafkaNewsPublishSender())
    handler.handle(current_time)


def flask():
    pass


flask()
