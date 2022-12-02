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


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service #
from webdriver_manager.chrome import ChromeDriverManager #



def YouTube_music(result):
    wd = webdriver.Chrome(service =Service(ChromeDriverManager().install()))


    search_name = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae"]
    #YouTube_URL = (f"https://www.youtube.com/results?search_query={search_name}")

    for i in range(0,9):
        wd.get(f"https://www.youtube.com/results?search_query={search_name[i]}")
        time.sleep(1)
    

    return

def main():
    result = []
    print("YouTubeMusic crawling >>>>>>>>>>>>>>>>>>>>")
    YouTube_music(result)

    #CB_tbl = pd.DataFrame(result,columns=('store','address','phone'))
    #CB_tbl.to_csv('./CoffeeBean.csv',encoding='utf-8',mode='w',index=True)

if __name__ == '__main__':
    main()
