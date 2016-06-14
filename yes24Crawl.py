from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup
import csv


def Yes24_Crawling():
    csv_file = open("yes24.csv","w")
    cw = csv.writer(csv_file, delimiter=',')
    cw.writerow(["Name","Price","PageNum","Weight","Volume"])
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

            if detailsoup.find("span", class_="cname") is not None: # 19세 이상 도서면 건너 뛰기
                bookname = detailsoup.find("span", class_="cname").next_sibling.next_element.next_element.next_element
            else :
                continue
            print("책 제목 : " + bookname)
            price = detailsoup.find("th", scope="row").next_sibling.next_element.next_element.strip()
            price = price.replace(",","")
            price = price.replace("원","")
            print("가격 : " + price)
            if pdSize = detailsoup.find("p", class_="pdSize") is not None:
                pdSize = detailsoup.find("p", class_="pdSize").next_element
            else :
                continue
            print("책 페이지 정보 : " + pdSize)

            if "쪽" not in pdSize:
                continue

            pdSizeList = pdSize.split("|")

            bookpage = "NA"
            bookweight = "NA"
            bookvolume = "NA"

            for j in range(len(pdSizeList)):
                if "쪽" in pdSizeList[j]:
                    bookpage = pdSizeList[j]
                    bookpage = bookpage.replace("쪽","")
                    bokkpage = bookpage.replace(" ","")
                elif "g" in pdSizeList[j]:
                    bookweight = pdSizeList[j]
                    bookweight = bookweight.replace(" ","")
                    bookweight = bookweight.replace("g","")
                else :
                    volumeList = []
                    pdSizeList[j] = pdSizeList[j].replace("mm","")
                    pdSizeList[j] = pdSizeList[j].replace(" ","")
                    volumeList = pdSizeList[j].split("*")
                    if len(volumeList) != 3 :
                        continue
                    else:
                        bookvolume = (int)(volumeList[0]) * (int)(volumeList[1]) * (int)(volumeList[2])

            print("페이지 수 : " + bookpage)
            print("무게 : " + bookweight)
            print("부피 : " + str(bookvolume))
            csv_file = open("yes24.csv","a")
            cw = csv.writer(csv_file, delimiter=',')
            cw.writerow([bookname, str(price), str(bookpage), str(bookweight), str(bookvolume)])


if __name__ == '__main__' :
    Yes24_Crawling()
