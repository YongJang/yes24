from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup
import csv


def Yes24_Crawling():
    csv_file = open("yes24.csv","a")
    cw = csv.writer(csv_file, delimiter=',',quotechar='|')
    cw.writerow(["제목","가격","페이지수","무게","부피"])
    for n in range(1,250):
        html = Request('http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06&fetchSize=40&PageNumber=' + str(n), headers={'User-Agent':'Mozilla/5.0'})
        webpage = urlopen(html).read()
        soup = BeautifulSoup(webpage, from_encoding="utf-8")
        bestsellers = soup.find_all("div" ,class_="goodsImgW")
        print(len(bestsellers))
        bestsellerLink = []
        for i in bestsellers:
            if i.find_all("a") is not None :
                bestsellerLink.append('http://www.yes24.com/'+i.find("a").get("href"))
        for i in range(len(bestsellerLink)):
            print("페이지 : " + bestsellerLink[i])
            detailhtml = Request(bestsellerLink[i])
            detailpage = urlopen(detailhtml).read()
            detailsoup = BeautifulSoup(detailpage, from_encoding="utf-8")
            bookname = detailsoup.find("span", class_="cname").next_sibling.next_element.next_element.next_element
            print("책 제목 : " + bookname)
            price = detailsoup.find("th", scope="row").next_sibling.next_element.next_element
            price = price.replace(" ","")
            price = price.replace("\n","")
            price = price.replace(",","")
            price = price.replace("원","")
            print("가격 : " + price)
            pdSize = detailsoup.find("p", class_="pdSize").next_element
            print("책 페이지 정보 : " + pdSize)
            pdSize = pdSize.replace(" ","")
            pdSize = pdSize.replace("쪽","")
            pdSize = pdSize.replace("g","")
            pdSize = pdSize.replace("mm","")
            pdSizeList = []
            pdSizeList = pdSize.split("|")
            bookpage = pdSizeList[0]
            bookweight = pdSizeList[1]
            print("페이지 수 : " + bookpage)
            print("무게 : " + bookweight)
            volumeList = []
            volumeList = pdSizeList[2].split("*")
            bookvolume = (int)(volumeList[0]) * (int)(volumeList[1]) * (int)(volumeList[2])

            print("부피 : " + str(bookvolume))


            cw.writerow([bookname, str(price), bookpage, bookweight, str(bookvolume)])


if __name__ == '__main__' :
    Yes24_Crawling()
