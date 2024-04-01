from bs4 import BeautifulSoup
import requests
import datetime
from datetime import datetime


class Rss_Coll(object):
    def __init__(self):
        '''Khoi tao truong gia tri tren RSS'''
        self.time = None
        self.file = []
        self.link = []
        self.date = []
        self.url = requests.get('https://vnexpress.net/rss/tin-moi-nhat.rss')
        self.soup = BeautifulSoup(self.url.content, 'xml')
        self.items = self.soup.find_all('item')
        self.items.reverse()
        self.last_num = int(open('last_num.txt', 'r').read())

    def time_index(self):
        for i, item in enumerate(self.items):
            time4 = item.pubDate.text
            # tao timestamp, du lieu luon moi khi cap nhat
            time1 = time4.split(" ")
            time2 = " ".join(["-".join([time1[3], '03', time1[1]]), time1[4]])
            date_format = '%Y-%m-%d %H:%M:%S'
            time3 = datetime.strptime(time2, date_format)
            timestamp = int(round(time3.timestamp()))
            if timestamp > self.last_num:
                # them gia tri link, dung try tanh gia tri rong
                try:
                    self.file.append({'Title': '{}'.format(item.title.text),
                                      'Link': '{}'.format(item.link.text),
                                      'Date': '{}'.format(item.pubDate.text),
                                      'Image': '{}'.format(item.enclosure['url'])})
                except:
                    pass

            if i == len(self.items) - 1 and timestamp > self.last_num:
                self.time = timestamp
                f = open('last_num.txt', 'w').write('{}'.format(self.time))
        return self.file


a = Rss_Coll()
a1 = a.time_index()

for i in a1:
    print(i['Image'])
