from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ReceivedNews:
    # news_id: str
    user_id: str
    received_at: datetime
    channel_id: str
    payload: dict = None


@dataclass
class ReceiveableNews:
    news_id: str
    payload: dict
    received_at: datetime
    acknowledged_at: datetime


class User:
    def __init__(self, user_id: str, name: str, channel_id: str, hourly_received_limit: str, payload: dict = None):
        self.__user_id = user_id
        self.__name = name
        self.__channel_id = channel_id
        self.__hourly_received_limit = int(hourly_received_limit)
        self.payload = payload

    @property
    def user_id(self) -> str:
        return self.__user_id

    def request_send_news(self, received_at: datetime,
                          current_received_news: int) -> Optional[ReceivedNews]:
        if not current_received_news >= self.__hourly_received_limit:
            return ReceivedNews(user_id=self.__user_id, received_at=received_at, channel_id=self.__channel_id, payload=self.payload)
        return None
