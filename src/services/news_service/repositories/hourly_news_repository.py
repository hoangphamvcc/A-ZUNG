from datetime import datetime
from typing import List

from src.services.news_service.domains import News
from src.services.news_service.handlers import HourlyNewsRepository
from .news_repository import MongoNewsRepository, MongoDB


class MongoHourlyNewsRepository(HourlyNewsRepository):
    def __init__(self):
        self.__news_repository = MongoNewsRepository()
        self.__news_collection = MongoDB().news

    def get_news(self, current_time: datetime) -> List[News]:
        # query news from mongo with public_at field, parse to News object
        pass

    def save_news(self, news: List[News]) -> bool:
        """
        The only way to persist news to database
        :param news:
        :return:
        """

        for item in news:
            self.__news_collection.update_one({
                '_id': item.news_id
            },
                {
                    "$set": item.to_dict()
                })

        return True
