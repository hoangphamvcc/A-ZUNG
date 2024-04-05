import time

import schedule

from src.services.news_service.handlers import VNExpressRSSHandler
from src.services.news_service.repositories import VNExpressRecentRSSRepository, MongoNewsRepository


def api():
    handler = VNExpressRSSHandler(VNExpressRecentRSSRepository(), MongoNewsRepository())
    saved_items = handler.handle()
    return {
        'message': 'success',
        'data': saved_items
    }, 200


def flask():
    pass


flask()
