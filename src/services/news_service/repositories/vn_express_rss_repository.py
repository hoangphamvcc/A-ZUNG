from typing import List

from src.services.news_service.domains import VNExpressRSS
from src.services.news_service.handlers import VNExpressRepository
import requests
from bs4 import BeautifulSoup


class VNExpressRecentRSSRepository(VNExpressRepository):
    def __init__(self):
        self.__url = 'https://vnexpress.net/rss/tin-moi-nhat.rss'

    def get_rss(self) -> List[VNExpressRSS]:
        # ap dung retry, handle connection exceptions
        data = requests.get(self.__url)
        soup = BeautifulSoup(data.content, 'xml')
        rss = [VNExpressRSS(item) for item in soup.find_all('item')]
        rss.reverse()

        return rss
