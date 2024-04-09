from datetime import datetime

from .vn_express_rss import FormattedNews
from dataclasses import dataclass


@dataclass
class PublishableNews:
    event_type: str
    payload: dict
    issued_at: datetime

    def to_dict(self) -> dict:
        return {
            "event_type": self.event_type,
            "payload": self.payload,
            # directly publish the datetime object may cause serialization issue
            "issued_at": self.issued_at
        }


class News:
    def __init__(self, news_id: str, title: str, link: str, public_at: str, rss_id: str, time_stamp: str,
                 is_published: bool):
        self.__news_id = news_id
        self.__title = title
        self.__link = link
        self.__public_at = public_at
        self.__rss_id = rss_id
        self.__time_stamp = time_stamp
        self.__is_published = is_published

    @property
    def news_id(self) -> str:
        return self.__news_id

    def to_dict(self) -> dict:
        return {
            "_id": self.__news_id,
            "title": self.__title,
            "link": self.__link,
            "public_at": self.__public_at,
            "rss_id": self.__rss_id,
            "time_stamp": self.__time_stamp,
            "is_published": self.__is_published
        }

    def to_formatted_news(self) -> FormattedNews:
        return FormattedNews(
            news_id=self.__news_id,
            title=self.__title,
            link=self.__link,
            date=self.__public_at,
            rss_id=self.__rss_id,
            time_stamp=self.__time_stamp
        )

    def to_publishable_news(self, issued_at: datetime = None) -> PublishableNews:
        return PublishableNews(
            event_type="publish_news",
            payload={
                "header": self.__title,
                "url": self.__link,
                "published_at": self.__public_at,
            },
            issued_at=issued_at or datetime.now()
        )

    def publish(self) -> bool:
        if not self.__is_published:
            self.__is_published = True

        return self.__is_published
