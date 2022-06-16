import requests

class Crawler:
    def __init__(self, base_url = "https://www.nasdaq.com/market-activity/stocks/snejf/historical"):
        self.base_url = base_url

    def get_html(self):
        r = requests.get(self.base_url)
        if r.ok:
            return r.text
        else:
            raise Exception("Server not found")


