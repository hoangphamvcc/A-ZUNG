from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class ReceivedNews:
    news_id: str
    user_id: str
    received_at: datetime
    channel_id: str


class User:
    def __init__(self, user_id: str, name: str, channel_id: str, hourly_received_limit: int):
        self.__user_id = user_id
        self.__name = name
        self.__channel_id = channel_id
        self.__hourly_received_limit = hourly_received_limit

    @property
    def user_id(self) -> str:
        return self.__user_id

    def request_send_news(self, news_id: str, received_at: datetime,
                          current_received_news: int) -> ReceivedNews:
        if not current_received_news >= self.__hourly_received_limit:
            return ReceivedNews(news_id, self.__user_id, received_at, self.__channel_id)
        return []
