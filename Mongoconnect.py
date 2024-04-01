import pymongo

myclient = pymongo.MongoClient("mongodb://10.0.67.162:27017/")
mydb = myclient['dev1']


