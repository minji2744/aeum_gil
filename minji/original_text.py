import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def chosun(soup):
    # 배롱님 감사합니다.
    pass

def donga(soup):
    return soup.find("div", attrs={"class":"article_txt"}).get_text()
    
def hani(soup):
    return soup.find("div", attrs={"class":"text"}).get_text()

def hankookilbo(soup):
    pass

def hankyung(soup):
    pass

def imbc(soup):
    pass

def kbs(soup):
    pass

def khan(soup):
    pass

def mk(soup):
    pass

def mt(soup):
    pass

def news1(soup):
    pass

def nocutnews(soup):
    pass

def sbs(soup):
    pass

def seoul(soup):
    pass

def yna(soup):
    pass

def ytn(soup):
    pass


headers = {
  "User-Agent":"" , # what is my user agent?
  "Accept-Language":"ko-KR,ko"
}
res = requests.get("??", headers=headers)
try: res.raise_for_status()
except:
    original = " <링크 접속 불가> "

res.encoding='UTF-8'
soup = BeautifulSoup(res.text, 'lxml')


article = soup.find("div", attrs={"class":"text"}).get_text()  # 텍스트 긁어오는 코드
print(article)
