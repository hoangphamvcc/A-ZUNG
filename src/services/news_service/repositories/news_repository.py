from src.services.news_service.domains import FormattedNews
from src.services.news_service.handlers import NewsRepository
import pymongo
from src.config import MONGO_URI, MONGO_DB_NAME, MONGO_NEWS_COLLECTION
import os

"""MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_NEWS_COLLECTION = os.getenv("MONGO_NEWS_COLLECTION")"""


class MongoDB:
    def __init__(self):
        self.__client = pymongo.MongoClient(MONGO_URI)
        self.db = self.__client[MONGO_DB_NAME]
        self.news = self.db[MONGO_NEWS_COLLECTION]


class MongoNewsRepository(NewsRepository):
    def __init__(self):
        self.__mongo = MongoDB()

    def is_id_existed(self, news_id: str) -> bool:
        result = self.__mongo.news.find({"_id": news_id})
        return next(result, None) is not None

    def save_news(self, news: FormattedNews):
        # Xy ly duplicate constraints     # done
        if not self.is_id_existed(news.news_id):
            self.__mongo.news.insert_one({
                '_id': news.news_id,
                'title': news.title,
                'link': news.link,
                'date': news.date,
                'rss_id': news.rss_id,
                'time_stamp': news.time_stamp
            })


class MemoryNewsRepository(NewsRepository):
    def __init__(self):
        self.__news = []

    def is_id_existed(self, news_id: str) -> bool:
        return news_id in [news.news_id for news in self.__news]

    def save_news(self, news: FormattedNews):
        print('save news')
        self.__news.append(news)
