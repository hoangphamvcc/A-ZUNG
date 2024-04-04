import pymongo

from bson.objectid import ObjectId


class mongoQuerry(object):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://10.0.67.162:27017/")
        self.db = self.client['task']
        self.news = self.db['News']
        self.a = 'a'

    def insert_one(self, collection: str, document: dict):
        self.db[f'{collection}'].insert_one(document)

    def status_find(self, collection: str):
        return next(self.db[f'{collection}'].find({'_id': '0'}))
    
    def scan_find(self,collection: str, query: dict):
        return next(self.db[f'{collection}'].find(query),None)

    def update_set(self, collection: str, query: dict, value: dict):
        self.db[f'{collection}'].update_one(query, {'$set': value})
    
    def find_all(self,collection: str):
        return self.db[f'{collection}'].find()
    
    def delete_one(self,collection: str, query: dict):
        self.db[f'{collection}'].delete_one(query)

    def test(self):
        print(self.a)


# demo
"""a = mongoQuerry().status_find('News')
print(a)"""
