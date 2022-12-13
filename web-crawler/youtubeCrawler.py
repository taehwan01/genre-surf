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


def scroll():    
    try:        
        # 페이지 내 스크롤 높이 받아오기
        last_page_height = wd.execute_script("return document.documentElement.scrollHeight")
        while True:
            # 임의의 페이지 로딩 시간 설정
            # PC환경에 따라 로딩시간 최적화를 통해 scraping 시간 단축 가능
            pause_time = random.uniform(1, 2)
            # 페이지 최하단까지 스크롤
            wd.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            # 페이지 로딩 대기
            time.sleep(pause_time)
            # 무한 스크롤 동작을 위해 살짝 위로 스크롤(i.e., 페이지를 위로 올렸다가 내리는 제스쳐)
            wd.execute_script("window.scrollTo(0, document.documentElement.scrollHeight-50)")
            time.sleep(pause_time)
            # 페이지 내 스크롤 높이 새롭게 받아오기
            new_page_height = wd.execute_script("return document.documentElement.scrollHeight")
            # 스크롤을 완료한 경우(더이상 페이지 높이 변화가 없는 경우 && result.length == 50)
            if new_page_height == last_page_height:
                print("스크롤 완료")
                break
            # 스크롤 완료하지 않은 경우, 최하단까지 스크롤
            else:
                last_page_height = new_page_height
    except Exception as e:
        print("에러 발생: ", e)
    
    

def YouTube_music(result):
    
    keyword ='blues'
    wd.get('https://youtube.com/');
    time.sleep(3)
    
    

    # keyword 입력
    search = wd.find_element(By.NAME, "search_query")
    time.sleep(2)
    search.send_keys(keyword) 
    #search.send_keys(Keys.ENTER)
    time.sleep(2)
    # search 버튼 클릭
    btnSearch = wd.find_element(By.ID, 'search-icon-legacy')
    btnSearch.click()
    print(keyword + "검색")
    time.sleep(3)

    # 검색 필터를 4k로 설정해서 shorts , 실시간 막을것
    #sfillter = wd.find_element(By.XPATH,'//*[@id="container"]/ytd-toggle-button-renderer/a')
    #sfillter.click()
    scroll()
      
    html = wd.page_source
    soupYM = BeautifulSoup(html,'html.parser')
    content_total = soupYM.find_all(class_ = 'yt-simple-endpoint style-scope ytd-video-renderer')
    content_total_title = list(map(lambda data: data.get_text().replace("\n", ""), content_total))
    content_total_link = list(map(lambda data: "https://youtube.com" + data["href"], content_total))
    content_play_time = list(map(lambda data: data['aria-label'],content_total))


    add_btn = soupYM.find_all(class_ = 'dropdown-trigger style-scope ytd-menu-renderer')

    new_content_total_time = []
    new_content_total_title = []
    new_content_total_link = []

    #for i in range(0,(len(content_play_time)-1)):
        #content_play_time[i] = content_play_time[i].split('전')
        #content_play_time[i] = content_play_time[i][1]
        #content_play_time[i] = content_play_time[i].split('조회수')
        #content_play_time[i] = content_play_time[i][0]
        #content_play_time[i] = content_play_time[i][0].strip()
        #print(content_play_time[i])
    #print(content_total_title)


    
    for i in range(0,(len(content_play_time)-1)):
        print(content_total_title[i])
        print(content_play_time[i])
        content_play_time[i] = content_play_time[i].split('전')
        content_play_time[i] = content_play_time[i][1]
        content_play_time[i] = content_play_time[i].split('분')
        content_play_time[i] = content_play_time[i][0]
        content_play_time[i] = re.sub(r'[^0-9]', '', content_play_time[i])
        print(content_play_time[i])
        if((int(content_play_time[i])>1) and (int(content_play_time[i])<7)):
            new_content_total_time.append(int(content_play_time[i]))
            new_content_total_title.append(content_total_title[i])
            new_content_total_link.append(content_total_link[i])
            #if(len(new_content_total_title) == 51):
                #continue
            result.append([content_total_title[i]] + [content_total_link[i]])
        print(new_content_total_time,new_content_total_title,new_content_total_link)
       


    


def main():
    result = []
    print("YouTubeMusic crawling >>>>>>>>>>>>>>>>>>>>")
    YouTube_music(result)

    CB_tbl = pd.DataFrame(result,columns=('title','link'))
    CB_tbl.to_csv('./YoutubeMusic.csv',encoding='utf-8',mode='w',index=True)

if __name__ == '__main__':
    main()
