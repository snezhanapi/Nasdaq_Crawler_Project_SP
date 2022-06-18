import requests
#share_name = input('Please choose share code\n')
#print(share_name)
from bs4 import BeautifulSoup as bs

class Crawler:
    def __init__(self, base_url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical'):
        self.base_url = base_url

    def get_html(self):
        print(self.base_url)
        r = requests.get('https://www.nasdaq.com/market-activity/stocks/aapl/historical')
        print(r.status_code)
        if r.ok:

            return r.text
        else:
            raise Exception("Server not found")

    def get_shares(self, html):
        soup = bs(html, 'html.parser')
        shares = soup.find('tbody', 'historical-data__table-body')
        print(shares)
        return shares

    def start(self):
        print("start")
        html = self.get_html()
        self.html = html
        print(html)
        #self.get_shares(html)


if __name__ == '__main__':
	stocks = Crawler()
	stocks.start()
