from datetime import datetime
from typing import List

from src.services.news_service.domains import News


class HourlyNewsRepository:
    """
    Query news within specific time and save them
    """

    def get_news(self, current_time: datetime) -> List[News]:
        pass

    def save_news(self, news: List[News]) -> bool:
        pass


class NewsPublishSender:
    """
    Send news to publisher
    """

    def send(self, news: News) -> bool:
        pass


class HourlyNewsPublishHandler:

    def __init__(self, news_repository: HourlyNewsRepository, sender: NewsPublishSender):
        self.__news_repository = news_repository
        self.__sender = sender

    def handle(self, current_time: datetime) -> bool:
        """
        Query news within specific time and publish them
        :param current_time:
        :return:
        """
        news = self.__news_repository.get_news(current_time)

        to_be_publishing_news = []
        for item in news:
            if item.publish():
                to_be_publishing_news.append(item)

        for item in to_be_publishing_news:
            self.__sender.send(item)

        return self.__news_repository.save_news(to_be_publishing_news)
