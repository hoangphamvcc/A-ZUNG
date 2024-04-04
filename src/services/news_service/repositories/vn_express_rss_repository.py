from typing import List

from src.services.news_service.domains import VNExpressRSS
from src.services.news_service.handlers import VNExpressRepository
from bs4 import BeautifulSoup
import src.config
from src.services.news_service.common import retry_request


class VNExpressRecentRSSRepository(VNExpressRepository):
    def __init__(self):
        self.__url = src.config.VNEXPRESS_URL

    def get_rss(self) -> List[VNExpressRSS]:
        # ap dung retry, handle connection exceptions  # done
        data = retry_request(self.__url)
        soup = BeautifulSoup(data.content, 'xml')
        rss = [VNExpressRSS(item) for item in soup.find_all('item')]
        rss.reverse()

        return rss
