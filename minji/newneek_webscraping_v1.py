'''
***프로젝트 설명***
'''

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
import time
import re
import csv

# 1. 웹데이터를 수집할 csv 파일을 만듭니다.
filename = "newneek.csv"
f = open(filename, "w", encoding='utf-8-sig', newline="")
writer = csv.writer(f)

title = "기사id 카테고리 제목 날짜 요약문 원문".split()  # column 에 대한 설명 첫행에 추가
writer.writerow(title)


# 2. selenium 과 BeautifulSoup을 활용해 크롤링을 진행합니다.
browser = webdriver.Chrome()   # selenium driver 크롬
url = "https://www.newneek.co"  # 뉴닉 페이지 이동
browser.get(url)

'''
# '더보기' 버튼이 나오지 않을 때까지 계속 누르기. 이후 동작이 잘 되면 주석을 풀고 코드를 실행합니다.
while True:
    time.sleep(2)
    try:
        browser.find_element_by_class_name("posts-pagination").click()  # 더보기 버튼 클릭
    except:
        break
'''

# 로딩이 완료된 후 card element 찾기
time.sleep(3)   # 로딩 시간
cards = browser.find_elements_by_class_name("card  ")   # 기사 card element 찾기

# https://www.newneek.co 의 기사들(card)을 하나씩 열며 진행합니다.
for idx, card in enumerate(cards):
    card.send_keys(Keys.COMMAND+"\n")   # card를 다른 탭으로 열기
    browser.switch_to_window(browser.window_handles[1])       # 새로 연 탭으로 이동
    
    time.sleep(2)   # 로딩 대기
    soup = BeautifulSoup(browser.page_source, 'lxml')    # soup 객체로 웹페이지 스크래핑
    
    # 각 기사의 카테고리, 제목, 날짜 데이터를 웹페이지로부터 수집합니다.
    try: # 카테고리
        category = soup.find("a", attrs={"class":"post-head-runninghead"}).get_text()
    except:
        category = 'NULL'  # 카테고리가 없는 기사의 경우는 'NULL'로 지정

    title = soup.find("h2", attrs={"class":"post-head-headline"}).get_text() # 제목
    date = soup.find("time", attrs={"class":"post-head-date"}).get_text()  # 날짜
    
    # 기사내용을 담은 paragraph 에서 요약문, 원문을 추출
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        try: 
            url = paragraph.find("a", attrs={"target":"_blank"})["href"]  # 원문 링크가 있는 paragraph만 추출
        except: continue
        
        sum = paragraph.get_text()   # 요약문 추출
        
        # 원문 가져오기
        headers = {
          "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
          "Accept-Language":"ko-KR,ko"
        }
        res = requests.get(url, headers=headers)
        try: res.raise_for_status()
        except: 
            original = " <링크 접속 불가> "
            continue
        res.encoding='UTF-8'

        s = BeautifulSoup(res.text, 'lxml')
        texts = s.find_all("p")
        original = ''
        for text in texts:
            original += text.get_text()
        original = re.sub(r'[\n\r\t]','', original)
        
        # csv의 row에 들어갈 data를 list변수로 생성
        data=[]
        data.extend((idx, category, title, date, sum, original))
        print(data)
        writer.writerow(data)  # csv 파일에 행으로 쓰기
    
    browser.close() # 현재 탭 닫기
    browser.switch_to_window(browser.window_handles[0]) # 첫번 째 탭(뉴닉 메인 페이지)으로 이동해서 다시 반복