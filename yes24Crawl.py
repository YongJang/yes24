from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup


def Yes24_Crawling():
    html = Request('http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06&fetchSize=40&PageNumber=1', headers={'User-Agent':'Mozilla/5.0'})

if __name__ == '__main__' :
    Yes24_Crawling()
