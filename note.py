

# conn = sqlite3.connect("pet_user.db")
# cur = conn.cursor()

# cur.execute("DELETE FROM schedule")

# cur.execute("SELECT foodname FROM userfood WHERE id == (?)", ('asdf', ))
# foodname = cur.fetchall()[0][0]

# print(foodname)
# conn.commit()
# # cur.execute("CREATE TABLE userinfo (id TEXT, location TEXT, email TEXT, img BLOB)")
# # cur.execute("CREATE TABLE userfood (id TEXT, foodname TEXT, wholefood REAL, eatfood REAL, dayfood REAL)")
# # cur.execute("ALTER TABLE userinfo ADD COLUMN foodname TEXT")
# # cur.execute("DROP TABLE userfood")
# cur.execute("SELECT img FROM userinfo WHERE id == (?)", ("af",))
# print(cur.fetchall())
# # print(cur.fetchall()[0][1])
# # print(cur.fetchall()[0][1])
# conn.commit()
# cur.close()

import requests
from bs4 import BeautifulSoup
import urllib

# searchWord = "삼성"
# req = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}'.format(searchWord), headers={'User-Agent':'Mozilla/5.0'})

# html = req.text

# soup = BeautifulSoup(html, 'html.parser')
# mytitle = soup.select(
#     "ul.type01 > li"
# )

# title = mytitle[0].select_one("a._sp_each_title").text
# source = mytitle[0].select_one("span._sp_each_source").text

# print(title)


# searchWord = "진돗개산책"
# req = requests.get('https://www.youtube.com/watch?v=rnybPdAFTuE', headers={'User-Agent':'Mozilla/5.0'})

# html = req.text

# soup = BeautifulSoup(html, 'html.parser')

# article = soup.find(
   
#     'yt-formatted-string'
# )

# print(article)
# container > div.router-output > app-base > search-box > div > div:nth-child(3) > div > weather-card > div > div:nth-child(1) > a.title

# root > div.sc-jAaTju.fNCBho.sc-jDwBTQ.efksxK > div.sc-feJyhm.kMGsFz > div > div > pre:nth-child(14) > code > span:nth-child(6)

#sp_nws1 > dl > dt > a

##sp_nws1 > dl > dt > a

##sp_nws1 > dl > dt > a

##contents//*[@id="contents"]
# searchWord = "서울시송파구동물병원"
# req = requests.get("https://map.naver.com/v5/search/{}".format(searchWord),  headers={'User-Agent':'Mozilla/5.0'})

# html = req.text

# soup = BeautifulSoup(html, 'html.parser')

# main = soup.find(
#     "div", {"class" : "ps-content"}
# )
# print(main)
# a= main[0].find("a")["href"]
# print(a)



# print(src)
# urllib.request.urlretrieve(src[0], "D:\\Desktop\\PYTHON\\숫자야구\\" + "a" + ".jpg")


import lxml
import time

import webbrowser
import requests
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("headless")
chromeDriverPath = "D:/Desktop/chromedriver.exe"
driver = webdriver.Chrome(chromeDriverPath, options = option)
searchWord = "서울시송파구동물병원"
# url = ("https://map.naver.com/v5/search/{}".format(searchWord), headers={'User-Agent':'Mozilla/5.0'})

driver.get("https://map.naver.com/v5/search/{}".format(searchWord))
time.sleep(3)
driver.find_element_by_xpath("//*[@id='container']/div[1]/shrinkable-layout/search-layout/search-list/search-list-contents/div/div[2]/button[2]").click()
time.sleep(1)
# soup = BeautifulSoup(driver.page_source, "html.parser")
# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# chromeDriverPath = "D:/Desktop/chromedriver.exe"
# driver = webdriver.Chrome(chromeDriverPath, options = option)

# searchWord = "서울시송파구동물병원"
# # url = ("https://map.naver.com/v5/search/{}".format(searchWord), headers={'User-Agent':'Mozilla/5.0'})

# driver.get("https://map.naver.com/v5/search/{}".format(searchWord))
# time.sleep(3)
# soup = BeautifulSoup(driver.page_source, "html.parser")
##container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-contents > div > div.pagination_area.search_pagination.ng-tns-c134-12 > button.btn_next.ng-tns-c134-12
title = driver.find_elements_by_css_selector(
            "div.list_search.ng-tns-c134-4 > search-item-place > div > div > div.title_box > strong.search_title"
            )
print (title[1].text)
# for i in range (4):
#     oneTitle = title[i].select_one(
#         "span.search_title_text"
#         ).text
#     print(oneTitle)

# phone = soup.select(
#     "div.list_search.ng-tns-c134-4 > search-item-place > div > div > div.search_text_box > span.phone"
# )
# for i in range (4):
#     onePhone = phone[i].text
#     print(onePhone)

# address = soup.select(
#     "div.list_search.ng-tns-c134-4 > search-item-place > div > div > div.search_text_box.ng-star-inserted > span"
# )
# for i in range (4):
#     oneAddress = address[i].text
#     print(oneAddress)
# address = soup[i].select(
#     "div.list_search.ng-tns-c134-4 > search-item.place > div > div > div.search_text_box.ng-star-inserted"
# )
# for i in range (3):
#     address = address[i].select(
#         "span.search_text.address"
#     ).text
#     print(address)


# for i in range (4):
#     title = hospital[i].select_one(
#         "span.search_title_text"
#     ).text

#     phone = hospital[i].select_one(
#         "span.search_text.phone.ng-star-inserted"
#     ).text

#     print(title)
#     print(phone)

#//*[@id="container"]/div[1]/shrinkable-layout/search-layout/search-list/search-list-contents/perfect-scrollbar/div/div[1]/div/div/div/search-item-place[1]/div/div[1]/div[2]/span[2]/text()

#/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/search-layout/search-list/search-list-contents/perfect-scrollbar/div/div[1]/div/div/div/search-item-place[2]/div/div[1]/div[2]/span[2]/text()
#container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-contents > perfect-scrollbar > div > div.ps-content > div > div > div