import pymongo
from bson.objectid import ObjectId
import random

client = pymongo.MongoClient("mongodb://10.0.67.162:27017/")

mydb = client['dev1']
my_collect = mydb['product_list']
pro_detail_collect = mydb['product_detail']

userdb = client['user']
list_user = userdb['User_detail']

event_collect = mydb['event']


def event_gen(id):
    user_id = random.randrange(1, 5)
    product_id = random.randrange(0, 5)
    option_id = random.randrange(1, 4)
    event = {'_id': '{}'.format(id),
             'User': 'User_{}'.format(user_id),
             'Product': 'Product_new_{}'.format(product_id),
             'Option': '{}'.format(option_id)}
    return event


def update_even(id):
    myquerry = {'_id': '0'}
    newvalues = {'$set': {'last-even': '{}'.format(id)}}
    event_collect.update_one(myquerry, newvalues)


"""First = {'_id': '0', 'last-even': '0', 'last-collect': '0'}
event_collect.insert_one(First)"""

"""for i in range(0, 5):
    a = event_gen()
    event_collect.insert_one(a)
    print(a)"""

status_document = next(event_collect.find({'_id': '0'}))
last_event = status_document['last-even']
print(type(last_event))
rand = random.randrange(1, 5)
curr_event = int(last_event)

for i in range(0, rand):
    a2 = curr_event + 1
    event_collect.insert_one((event_gen(a2)))
update_even(curr_event)

for x in event_collect.find():
    print(x)
