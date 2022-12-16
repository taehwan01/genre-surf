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
    time.sleep(5)

    timefillter = wd.find_element(By.XPATH, '//html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[3]/ytd-search-filter-renderer[3]/a')
    timefillter.click()
    time.sleep(5)


    html = wd.page_source
    soupYM = BeautifulSoup(html,'html.parser')
    body = wd.find_element(By.CSS_SELECTOR,'body')


    add_btn = []

    content_total = soupYM.find_all(class_ = 'style-scope ytd-thumbnail-overlay-time-status-renderer')
    content_total = list(map(lambda data: data.get_text().replace("\n", ""), content_total))

    #content_play_time = list(map(lambda data: data.get_text().replace("\n", ""), content_total))
    #content_play_time = content_play_time[1::2]
    #content_play_time[i] = content_play_time[i].strip()
    #print(content_play_time)
            

    for i in range(0,(len(content_total)-1)):
        add_btn.append(wd.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer['+str(i+1)+']/div[1]/div/div[1]/div/div/ytd-menu-renderer/yt-icon-button/button'))
        add_btn[i].click()
        time.sleep(3)
        add_btn_select = wd.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[1]')
        add_btn_select.click()
        wd.execute_script("window.scrollTo(" + str(i*220)+ "," +  str((i+1)*220) + ");")
        time.sleep(5)

        # total_time == 24시간
        if(i == 4) :
            body.send_keys('k')
            break

    print("크롤링 종료")


            
#    content_total = soupYM.find_all(class_ = 'yt-simple-endpoint style-scope ytd-video-renderer')
#    content_total_title = list(map(lambda data: data.get_text().replace("\n", ""), content_total))
#    content_total_link = list(map(lambda data: "https://youtube.com" + data["href"], content_total))
#    content_play_time = list(map(lambda data: data['aria-label'],content_total))
#    new_content_total_time = []
#   new_content_total_title = []
#    new_content_total_link = []
#    for i in range(0,(len(content_play_time)-1)):
#        print(content_total_title[i])
#        print(content_play_time[i])
#        content_play_time[i] = content_play_time[i].split('전')
#        content_play_time[i] = content_play_time[i][1]
#       content_play_time[i] = content_play_time[i].split('분')
#        content_play_time[i] = content_play_time[i][0]
#        content_play_time[i] = re.sub(r'[^0-9]', '', content_play_time[i])
#        print(content_play_time[i])
#        if((int(content_play_time[i])>1) and (int(content_play_time[i])<7)):
#           new_content_total_time.append(int(content_play_time[i]))
#            new_content_total_title.append(content_total_title[i])
#            new_content_total_link.append(content_total_link[i])
            #if(len(new_content_total_title) == 51):
                #continue
#            result.append([content_total_title[i]] + [content_total_link[i]])
#        print(new_content_total_time,new_content_total_title,new_content_total_link)
       


    
def main():
    result = []
    print("YouTubeMusic crawling >>>>>>>>>>>>>>>>>>>>")
    YouTube_music()

if __name__ == '__main__':
    main()
