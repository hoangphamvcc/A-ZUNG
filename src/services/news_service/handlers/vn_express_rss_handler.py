from typing import List

from src.services.news_service.domains import VNExpressRSS, FormattedNews


class VNExpressRepository:
    """
    Request layer for VNExpress RSS
    """

    def get_rss(self) -> List[VNExpressRSS]:
        pass


class NewsRepository:
    """
    Persistence layer for news
    """

    def is_id_existed(self, news_id: str) -> bool:
        """
        Check if news_id existed in database
        :param news_id:
        :return: True if existed, False otherwise
        """
        pass

    def save_news(self, news: FormattedNews):
        pass


class VNExpressRSSHandler:
    def __init__(self, vn_express_repository: VNExpressRepository, news_repository: NewsRepository):
        self.__news_repository = news_repository
        self.__vn_express_repository = vn_express_repository

    def handle(self) -> List[FormattedNews]:
        """
        Handle request rss and save unique news to database
        :return: Number of saved news
        """
        raw_rss = self.__vn_express_repository.get_rss()
        news = [rss.to_formatted_news() for rss in raw_rss]

        saved_formatted_news = []
        for item in news:
            if not self.__news_repository.is_id_existed(item.rss_id):
                saved_formatted_news.append(item)

        # To prevent exception during saving
        for saved_item in saved_formatted_news:
            self.__news_repository.save_news(saved_item)

        return saved_formatted_news
