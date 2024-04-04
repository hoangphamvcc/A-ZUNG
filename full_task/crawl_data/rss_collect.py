from bs4 import BeautifulSoup
import requests
import datetime
from datetime import datetime


class RssColl(object):
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
        self.last_num = 1
        self.id = None

    def time_index(self):
        for i, item in enumerate(self.items):
            link_origin = item.link.text
            # tao id_link, du lieu luon moi khi cap nhat
            link_split_html = link_origin.split('.html')[0]
            self.id = link_split_html.split('-')[-1]
            # tao timestamp, du lieu luon moi khi cap nhat
            time_origin = item.pubDate.text
            time_split = time_origin.split(" ")
            time_data = " ".join(["-".join([time_split[3], '03', time_split[1]]), time_split[4]])
            date_format = '%Y-%m-%d %H:%M:%S'
            time_dataform = datetime.strptime(time_data, date_format)
            timestamp = int(round(time_dataform.timestamp()))


            try:
                self.file.append({'Title': f'{item.title.text}',
                                  'Link': f'{item.link.text}',
                                  'Date': f'{item.pubDate.text}',
                                  'Rss_id': f'{self.id}',
                                  'Time_stamp': f'{timestamp}'})
            except:
                pass
        return self.file


"""
            if i == len(self.items) - 1 and timestamp > self.last_num:
                self.time = timestamp
                f = open('last_num.txt', 'w').write('{}'.format(self.time))"""


a = RssColl()
a1 = a.time_index()
print(a1)
