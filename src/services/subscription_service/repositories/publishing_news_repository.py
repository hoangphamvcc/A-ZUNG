from datetime import datetime
from typing import List

import requests

from src.config import MONGO_URI, MONGO_DB_NAME, MONGO_USER_COLLECTION, MONGO_RECEIVED_NEWS_COLLECTION
from src.services.subscription_service.domains import User, ReceivedNews
from src.services.subscription_service.handlers import PublishingNewsRepository, PublishClient
import pymongo


class MongoDB:
    def __init__(self):
        self.__client = pymongo.MongoClient(MONGO_URI)
        self.db = self.__client[MONGO_DB_NAME]
        self.users = self.db[MONGO_USER_COLLECTION]
        self.receive_news = self.db[MONGO_RECEIVED_NEWS_COLLECTION]


class MongoPublishingNewsRepository(PublishingNewsRepository):
    def __init__(self, mongo_client: MongoDB):
        self.__mongo_client = mongo_client

    def get_all_users(self) -> List[User]:
        results = self.__mongo_client.users.find()
        users = []
        while True:
            result = next(results, None)
            if result is None:
                break

            users.append(User(user_id=result['_id'], name=result['name'], channel_id=result['channel_id'],
                              hourly_received_limit=result['hourly_received_limit']))

        return users

    def save(self, news: List[ReceivedNews]):
        for new in news:
            self.__mongo_client.receive_news.insert_one({
                'news_id': new.news_id,
                'user_id': new.user_id,
                'received_at': new.received_at
            })

    def get_current_hourly_received_news(self, user_id: str, received_at: datetime) -> int:
        start_hour = received_at.replace(minute=0, second=0, microsecond=0)
        end_hour = start_hour.replace(hour=start_hour.hour + 1)
        return self.__mongo_client.receive_news.count({
            'user_id': user_id,
            'received_at': {
                '$gte': start_hour,
                '$lt': end_hour
            }
        })


class TelegramPublishClient(PublishClient):

    def publish(self, news: List[ReceivedNews]):
        # send news data with telegram get api
        for item in news:
            url = "https://api.telegram.org/bot{token}/sendMessage".format(token=item.channel_id)
            data = {
                # Format them
                'chat_id': item.user_id,
                'text': f"New news: {item.news_id} at {item.received_at}"
            }
            requests.post(url, data=data)
