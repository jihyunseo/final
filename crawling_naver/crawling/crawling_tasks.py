from background_task import background
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests 
import sqlite3
import time
import csv
import re 



# #DB
# conn = sqlite3.connect("db.sqlite3")
# #Table 
# query = 'CREATE TABLE coin (text TEXT)'
# conn.execute(query)

@background # add

def task_crawling_naver(schedule=2, repeat=3600): #Schedule->start from now on, repeat->timeset(sec) 
    url ='https://m.search.naver.com/search.naver?where=m_realtime&query=%EB%B9%A8%EB%9E%98%EB%B0%A9&sm=mtb_opt&section=0&best=0&nso=so%3Ar%2Cp%3A1h' #naver 실시간 키워드 검색['빨래방']
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('div', class_='desc_txt') #본문class
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            text = ''
            for link in links:
             text = str.strip(link.get_text())    
              #   print(text)    
             cur.execute("INSERT INTO coin (text) VALUES (?)",(text,)) #단일 데이터 삽입할 경우 ,로 구분자 설정
             con.commit()
             print('laundryshop  : ', type(links), len(links))
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
   
    print('task_crawling_naver : ', type(links), len(links), time_str)




@background # add
def task_crawling_naver2(schedule=10, repeat=3600): #Schedule->start from now on, repeat->timeset(sec) 
    url1 ='https://m.search.naver.com/search.naver?where=m_realtime&query=%EC%84%B8%ED%83%81%EB%B0%A9&sm=mtb_opt&section=0&best=0&nso=so%3Ar%2Cp%3A1h' #naver 리얼타임 키워드 검색['세탁방']
    res1 = requests.get(url1, headers={"User-Agent": "Mozilla/5.0"})
    if res1.status_code == 200:
        soup = BeautifulSoup(res1.content, 'html.parser')
        links = soup.find_all('div', class_='desc_txt') #본문class
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            text = ''
            for link in links:
             text = str.strip(link.get_text())    
              #   print(text)    
             cur.execute("INSERT INTO coin (text) VALUES (?)",(text,)) #단일 데이터 삽입할 경우 ,로 구분자 설정
             con.commit()
             print('laundryshop  : ', type(links), len(links))
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
   
    print('task_crawling_naver2 : ', type(links), len(links), time_str)