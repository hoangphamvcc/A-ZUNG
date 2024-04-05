from typing import List

from src.services.news_service.domains import VNExpressRSS
from src.services.news_service.handlers import VNExpressRepository
from bs4 import BeautifulSoup
from src.config import VNEXPRESS_URL
from src.services.news_service.common import retry_request


class VNExpressRecentRSSRepository(VNExpressRepository):
    def __init__(self):
        self.__url = VNEXPRESS_URL

    def get_rss(self) -> List[VNExpressRSS]:
        # ap dung retry, handle connection exceptions  # done
        data = retry_request(self.__url)
        soup = BeautifulSoup(data.content, 'xml')
        rss = [VNExpressRSS(item) for item in soup.find_all('item')]
        rss.reverse()
        print('get_rss')

        return rss
