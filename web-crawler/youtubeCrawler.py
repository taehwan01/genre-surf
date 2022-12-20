# 이 폴더 clone 해서 받았으면,
# git checkout -b [너 git 아이디]
# 위 명령어로 너의 브랜치를 하나 파고 이 브랜치 안에서 네 코드들 작성해
# 이 폴더 안에서 소스파일들 너가 원하는대로 생성해서 파일 작성해
# 파일은 최대한 한 기능마다 또는 한 함수마다 commit 남기고
# commit 방식은 아래 예시처럼
# feat(youtube-music-crawler): 웹 호출하여 데이터 추출
# feat(youtube-music-crawler): 웹에서 가져온 데이터 가공
# commit 메시지는 인터넷에서 "git commit 메시지" 치면 다 나오는데, feat, style, docs, refactor 등등 다양해
# 커밋 메시지 중에서 너가 알맞는 거 고르고, 너는 유튜브 뮤직 웹 크롤링 담당하기로 했으니까 feat(youtube-music-crawler) 이런 식으로 괄호에 담당하는 부분들 남겨
import time

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
import random
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service #
from webdriver_manager.chrome import ChromeDriverManager #
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


wd = webdriver.Chrome(service =Service(ChromeDriverManager().install()))
    
    
def YouTube_music():

    keyword ='pop genre song'
    wd.get('https://youtube.com/');


    search = wd.find_element(By.NAME, "search_query")
    time.sleep(2)
    search.send_keys(keyword)

    btnSearch = wd.find_element(By.ID, 'search-icon-legacy')
    btnSearch.click()
    print(keyword + "검색")
    time.sleep(3)


    fillter = wd.find_element(By.XPATH,'//*[@id="container"]/ytd-toggle-button-renderer')
    fillter.click()
    time.sleep(3)

    timefillter_1 = wd.find_element(By.XPATH, '//html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[3]/ytd-search-filter-renderer[3]/a')
    timefillter_1.click()
    time.sleep(3)

    fillter = wd.find_element(By.XPATH,'//*[@id="container"]/ytd-toggle-button-renderer')
    fillter.click()
    time.sleep(3)


    timefillter_2 = wd.find_element(By.XPATH, '//html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[4]/ytd-search-filter-renderer[2]/a')
    timefillter_2.click()
    time.sleep(3)


    html = wd.page_source
    soupYM = BeautifulSoup(html,'html.parser')
    body = wd.find_element(By.CSS_SELECTOR,'body')


    add_btn = []
            
    i = 0
    total_hour = 0
    total_minute = 0
    while True:

        add_btn.append(wd.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer['+str(i+1)+']/div[1]/div/div[1]/div/div/ytd-menu-renderer/yt-icon-button/button'))
        add_btn[i].click()
        time.sleep(3)

        content_time = wd.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-video-renderer['+str(i+1)+']/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span').text

        
        add_btn_select = wd.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[1]')
        add_btn_select.click()
            
      
        if(len(content_time) < 6):
            content_time = '00:'+str(content_time)
            
        print('영상시간 :' + content_time)    
        content_time = datetime.strptime(content_time,"%H:%M:%S")
        total_hour = total_hour + content_time.hour
        total_minute = total_minute + content_time.minute
        #print(total_hour)
        #print(total_minute)

        if(total_minute > 60 or total_minute == 60):
            total_minute = total_minute - 60
            total_hour = total_hour + 1
        
        time.sleep(3)
        wd.execute_script("window.scrollTo(" + str(i*220)+ "," +  str((i+1)*220) + ");")

        
        
        i = i + 1
        time.sleep(5)

        if(total_hour > 23) :
            body.send_keys('k')
            break
        

    print("크롤링 종료")
        
    
def main():
    result = []
    print("YouTubeMusic crawling >>>>>>>>>>>>>>>>>>>>")
    YouTube_music()

if __name__ == '__main__':
    main()
