from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.services.subscription_service.domains import ReceivedNews, User


@dataclass
class PublishingNewsCommand:
    url: str
    header: str
    news_id: str
    published_at: datetime


class PublishingNewsRepository:
    def get_all_users(self) -> List[User]:
        pass

    def save(self, news: List[ReceivedNews]):
        pass

    def get_current_hourly_received_news(self, user_id: str, received_at: datetime) -> int:
        pass


class PublishClient:
    def publish(self, news: List[ReceivedNews]):
        pass


class PublishingNewsHandler:
    def __init__(self, repository: PublishingNewsRepository, client: PublishClient):
        self.__repository = repository
        self.__client = client

    def handle(self, command: PublishingNewsCommand):
        print(f"Publishing news: {command.header} at {command.published_at} with url: {command.url}")
        current_subscribe_users = self.__repository.get_all_users()
        received_news = []
        receiving_time = datetime.now()
        for user in current_subscribe_users:
            current_received_news = self.__repository.get_current_hourly_received_news(user.user_id, receiving_time)
            received_news.append(user.request_send_news(command.news_id, datetime.now(), current_received_news))

        self.__repository.save(received_news)
        for user in current_subscribe_users:
            self.__client.publish(received_news)
