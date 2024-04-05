import dataclasses


@dataclasses.dataclass
class FormattedNews:
    news_id: str
    title: str
    link: str
    date: str
    rss_id: str
    time_stamp: str

    def create_new_id(self):
        # Create common news id for all rss types of news
        pass


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
            date=self.__item.pubDate.text,
            rss_id=link_origin.split('.html')[0].split('-')[-1],
            time_stamp=self.__item.pubDate.text
        )
