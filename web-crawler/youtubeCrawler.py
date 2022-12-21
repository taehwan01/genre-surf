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


    
    
def YouTube_music():


    # wd.get(url) 을 이용하여 유튜브 open
    wd = webdriver.Chrome(service =Service(ChromeDriverManager().install()))

    wd.get('https://youtube.com/');
    keyword ='blues genre song'

    # search query로 음악 장르를 받아서 검색어 입력 
    search = wd.find_element(By.NAME, "search_query")
    time.sleep(2)
    search.send_keys(keyword)

    # 검색 버튼의 요소를 찾아서 저장하 클릭
    btnSearch = wd.find_element(By.ID, 'search-icon-legacy')
    btnSearch.click()
    print(keyword + "검색")
    time.sleep(3)


    # 조건 필터 버튼 클릭
    fillter = wd.find_element(By.XPATH,'//*[@id="container"]/ytd-toggle-button-renderer')
    fillter.click()
    time.sleep(3)

    # 시간 조건 필터
    timefillter_1 = wd.find_element(By.XPATH, '//html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[3]/ytd-search-filter-renderer[3]/a')
    timefillter_1.click()
    time.sleep(3)

    # 조건 필터 버튼 클릭
    fillter = wd.find_element(By.XPATH,'//*[@id="container"]/ytd-toggle-button-renderer')
    fillter.click()
    time.sleep(3)

    # 4K 필터 버튼 클릭
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

        # 영상의 더보기 버튼 저장 , 클릭
        add_btn.append(wd.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer['+str(i+1)+']/div[1]/div/div[1]/div/div/ytd-menu-renderer/yt-icon-button/button'))
        add_btn[i].click()
        time.sleep(3)

        # 영상 길이 저장
        content_time = wd.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer['+str(i+1)+']/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span').text

        # 현재재생리스트 추가 
        add_btn_select = wd.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[1]')
        add_btn_select.click()
            

        # 영상 시간 문자열을 시간화
        if(len(content_time) < 6):
            content_time = '00:'+str(content_time)
            
        print('영상시간 :' + content_time)    
        content_time = datetime.strptime(content_time,"%H:%M:%S")

        # 재생리스트 전체 시간 , 전체 분 계산 
        total_hour = total_hour + content_time.hour
        total_minute = total_minute + content_time.minute
        #print(total_hour)
        #print(total_minute)

        if(total_minute > 60 or total_minute == 60):
            total_minute = total_minute - 60
            total_hour = total_hour + 1
        
        time.sleep(3)

        # 영상 썸네일의 높이만큼 아래로 스크롤  
        wd.execute_script("window.scrollTo(" + str(i*220)+ "," +  str((i+1)*220) + ");")

          
        i = i + 1
        time.sleep(5)

        # 현재 재생목록이 24시간 (하루) 가되면 웹크롤링 종료
        if(total_hour > 24) :
            
            body.send_keys('k')
            time.sleep(10)

            # 광고 제거
            skip_btn = wd.find_element(By.XPATH,'/html/body/ytd-app/ytd-miniplayer/div[2]/div/div[1]/div[1]/div/ytd-player/div/div/div[21]/div/div[3]/div/div[2]/span/button')
            skip_btn.click()
            break
        

    print("크롤링 종료")
        
    
def main():
    print("YouTube crawling >>>>>>>>>>>>>>>>>>>>")
    YouTube_music()

if __name__ == '__main__':
    main()
