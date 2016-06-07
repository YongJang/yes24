from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup


def Yes24_Crawling():
    n = 1
    html = Request('http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06&fetchSize=40&PageNumber=' + str(n), headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(html).read()
    soup = BeautifulSoup(webpage , from_encoding="utf-8")
    # //*[@id="category_layout"]/tbody/tr[1]/td[2]/div/a[1]
    # //*[@id="category_layout"]/tbody/tr[3]/td[2]/div/a[1]
    # //*[@id="category_layout"]/tbody/tr[5]/td[2]/div/a[1]
    bestsellers = soup.find_all("div" ,class_="goodsImgW")
    print(len(bestsellers))
    bestsellerLink = []
    for i in bestsellers:
        if i.find_all("a") is not None :
            bestsellerLink.append(i.find_all("a"))
    for i in range(len(bestsellerLink)):
        print(bestsellerLink[i])

if __name__ == '__main__' :
    Yes24_Crawling()
