from src.services.news_service.domains import FormattedNews
from src.services.news_service.handlers import NewsRepository
import pymongo

import os

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_NEWS_COLLECTION = os.getenv("MONGO_NEWS_COLLECTION")


class MongoDB:
    def __init__(self):
        self.__client = pymongo.MongoClient(MONGO_URI)
        self.db = self.__client[MONGO_DB_NAME]
        self.news = self.db[MONGO_NEWS_COLLECTION]


class MongoNewsRepository(NewsRepository):
    def __init__(self):
        self.__mongo = MongoDB()

    def is_id_existed(self, news_id: str) -> bool:
        result = self.__mongo.news.find_one({"_id": news_id})
        return next(result, None) is not None

    def save_news(self, news: FormattedNews):
        # Xy ly duplicate constraints
        self.__mongo.news.insert_one({
            '_id': news.news_id,
            'title': news.title,
            'link': news.link,
            'public_at': news.date,
            'rss_id': news.rss_id,
            'time_stamp': news.time_stamp,
            'is_published': False
        })


class MemoryNewsRepository(NewsRepository):
    def __init__(self):
        self.__news = []

    def is_id_existed(self, news_id: str) -> bool:
        return news_id in [news.news_id for news in self.__news]

    def save_news(self, news: FormattedNews):
        self.__news.append(news)
