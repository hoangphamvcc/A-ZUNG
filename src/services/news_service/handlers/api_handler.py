from datetime import datetime
from src.common import datetimestr_to_datetime


class MongoDBSearch():

    def __init__(self, db):
        self.__mongo = db

    def hour_page_limit(self, hour, page, limit):
        pass
