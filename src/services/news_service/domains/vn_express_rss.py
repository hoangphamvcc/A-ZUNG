import dataclasses
from datetime import datetime


@dataclasses.dataclass
class FormattedNews:
    news_id: str
    title: str
    link: str
    public_at: str
    rss_id: str
    time_stamp: str
    is_published: bool

    def to_datetime(self) -> datetime:
        return datetime.strptime(self.public_at, '%a, %d %b %Y %H:%M:%S %z')


class VNExpressRSS:
    def __init__(self, item):
        self.__item = item

    def to_formatted_news(self) -> FormattedNews:
        # Format item to FormattedNews
        # time_index_function
        link_origin = self.__item.link.text
        # news id
        # create object id
        return FormattedNews(
            news_id=link_origin.split('.html')[0].split('-')[-1],
            title=self.__item.title.text,
            link=link_origin,
            public_at=self.__item.pubDate.text,
            rss_id=link_origin.split('.html')[0].split('-')[-1],
            time_stamp=self.__item.pubDate.text,
            is_published=False
        )
