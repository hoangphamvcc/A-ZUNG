from datetime import datetime
from typing import List

from src.services.news_service.domains import News
from src.services.news_service.handlers import HourlyNewsRepository
from .news_repository import MongoNewsRepository, MongoDB


class MongoHourlyNewsRepository(HourlyNewsRepository):
    def __init__(self):
        self.__news_repository = MongoNewsRepository()
        self.__news_collection = MongoDB().news

    def get_unpulished_news(self, current_time: datetime) -> List[News]:
        # query news from mongo with public_at field, parse to News object
        start_hour = current_time.replace(minute=0, second=0, microsecond=0)
        end_hour = start_hour.replace(hour=start_hour.hour + 1)

        results = self.__news_collection.aggregate([
            {
                "$match": {
                    # "public_at": {
                    #     "$gte": start_hour,
                    #     "$lt": end_hour
                    # },
                    "is_published": False
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "title": 1,
                    "link": 1,
                    "public_at": 1,
                    "rss_id": 1,
                    "time_stamp": 1,
                    "is_published": 1
                }
            }
        ])

        return [News(
            news_id=item['_id'],
            title=item['title'],
            link=item['link'],
            public_at=item['public_at'],
            rss_id=item['rss_id'],
            time_stamp=item['time_stamp'],
            is_published=item['is_published']
        ) for item in list(results)]

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
