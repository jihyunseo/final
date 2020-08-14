from background_task import background
from selenium import webdriver # 로그인 기능 필요한 경우 사용  -> webdriver.Chrome()
from bs4 import BeautifulSoup
import pandas as pd
import requests 
import sqlite3
import time
import re
import csv 


url ='https://m.search.naver.com/search.naver?where=m_realtime&query=%EB%B9%A8%EB%9E%98%EB%B0%A9&sm=mtb_opt&section=0&best=0&nso=so%3Ar%2Cp%3A1h'
res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# conn = sqlite3.connect("db.sqlite3")
# query = 'CREATE TABLE coin (text TEXT)'
# conn.execute(query)

@background # add
def task_crawling_naver(schedule=0, repeat=3600): #Schedule->start from now on, repeat->timeset(sec) 
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('div', class_='desc_txt')
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            text = ''
            for link in links:
             text = str.strip(link.get_text())    
              #   print(text)    
             cur.execute("INSERT INTO coin (text) VALUES (?)",(text,))
             con.commit()
             print('laundryshop  : ', type(links), len(links))
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
   
    print('task_crawling_naver : ', type(links), len(links), time_str)


# conn = sqlite3.connect('db.sqlite3')
# query = 'CREATE TABLE breakingIT (title TEXT, link TEXT)'
# conn.execute(query)
# conn.commit(); conn.close()
# res = requests.get('https://news.daum.net/breakingnews/digital')
# @background # add
# def task_crawling_daum(schedule=5, repeat=60*3):
#     if res.status_code == 200:
#         soup = BeautifulSoup(res.content, 'html.parser')
#         links = soup.find_all('a', class_='link_txt')
#         with sqlite3.connect("db.sqlite3") as con:
#             cur = con.cursor()
#             title = str(); link = str()
#             for link in links:
#                 title = str.strip(link.get_text())
#                 link = link.get('href')
#                 cur.execute("INSERT INTO breakingIT (title,link) VALUES (?,?)",(title,link))
#             con.commit()
#         print('task_crawling_daum : ', type(links), len(links))


#     time_tuple = time.localtime()
#     time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    
#     print('task_crawling_daum : ', type(links), len(links), time_str)


# driver = webdriver.Chrome(executable_path='/home/sundooedu/Downloads/chromedriver') 
# contents_list =[]

# url='https://news.v.daum.net/v/20200803110700631'


# for i in range(10):
#     driver.get(url) 
#     print(driver.current_url)
#     time.sleep(3)
#     try:
#          while driver.find_element_by_xpath('//*[@id="alex-area"]/div/div/div/div[3]/div[2]/a').text !='':
#              driver.find_element_by_xpath('//*[@id="alex-area"]/div/div/div/div[3]/div[2]/a').click()
#              time.sleep(3)
#     except:
#         pass
#     for k in range(40):
#         try:
#             contents = driver.find_element_by_xpath
#             ('/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div[6]/div[2]/div/div/div/div[3]/ul[2]/li[' +str(k)+']/div/p').text
#             contents = contents.replace("\n"," ")
#             contents_list.append(contents)
#         except:
#             pass
#     time.sleep(3)

# contents_list
# conn = sqlite3.connect('db.sqlite3')
# query = 'CREATE TABLE realtimeDryer (title TEXT, link TEXT)'
# conn.execute(query)
# conn.commit(); conn.close()
# res = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=realtime&query=%EA%B1%B4%EC%A1%B0%EA%B8%B0&oquery=%EA%B1%B4%EC%A1%B0&tqi=UxCNmwp0JywssEfSWg8ssssssps-289489')
# @background # add
# def task_crawling_daum(schedule=5, repeat=60*3):
#     if res.status_code == 200:
#         soup = BeautifulSoup(res.content, 'html.parser')
#         links = soup.find_all('a', class_='link_txt')
#         with sqlite3.connect("db.sqlite3") as con:
#             cur = con.cursor()
#             title = str(); link = str()
#             for link in links:
#                 title = str.strip(link.get_text())
#                 link = link.get('href')
#                 cur.execute("INSERT INTO realtimeDryer (title,link) VALUES (?,?)",(title,link))
#             con.commit()
#         print('task_crawling_daum : ', type(links), len(links))


#     time_tuple = time.localtime()
#     time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    
#     print('task_crawling_daum : ', type(links), len(links), time_str)

# conn = sqlite3.connect('db.sqlite3')
# query = 'CREATE TABLE breakingIT (title TEXT, link TEXT)'
# conn.execute(query)
# conn.commit(); conn.close()
# res = requests.get('https://news.daum.net/breakingnews/digital')
# @background # add
# def task_crawling_daum(schedule=5, repeat=60*3):
#     if res.status_code == 200:
#         soup = BeautifulSoup(res.content, 'html.parser')
#         links = soup.find_all('a', class_='link_txt')
#         with sqlite3.connect("db.sqlite3") as con:
#             cur = con.cursor()
#             title = str(); link = str()
#             for link in links:
#                 title = str.strip(link.get_text())
#                 link = link.get('href')
#                 cur.execute("INSERT INTO breakingIT (title,link) VALUES (?,?)",(title,link))
#             con.commit()
#         print('task_crawling_daum : ', type(links), len(links))


#     time_tuple = time.localtime()
#     time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    
#     print('task_crawling_daum : ', type(links), len(links), time_str)