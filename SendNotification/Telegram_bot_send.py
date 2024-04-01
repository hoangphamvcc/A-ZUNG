import requests


class Bot_send(object):
    def __init__(self, message):
        """Tao gio tri mac dinh cho Bot; send bang tinh nang send"""
        self.message = message
        self.TOKEN = "7093067808:AAEfPz21IUweO0uH2Afu1y_V5Mrc_8cdohs"
        self.CHAT_ID1 = "-1002004471961"

    def send(self):
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.CHAT_ID1}&parse_mode=Markdown&text={self.message}"
        r = requests.get(url)
        return r.json()
