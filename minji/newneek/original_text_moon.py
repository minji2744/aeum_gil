import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def chosun(browser):  # 조선일보, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "article-body"))).text
    browser.execute_script("window.stop();")
    return original

def donga(browser):  # 동아일보
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "article_txt"))).text
    browser.execute_script("window.stop();")
    return original
    
def hani(browser):  # 한겨레신문, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='a-left-scroll-in']/div[2]/div/div[2]"))).text
    browser.execute_script("window.stop();")
    return original

def hankookilbo(browser):  # 한국일보
    texts = WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "editor-p")))
    browser.execute_script("window.stop();")
    original = ''
    for text in texts:
        original = original + text.text + ' '
    return original

def yna(browser):  # 연합뉴스, 확인 (조금 문제 있음)
    try: original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleWrap"]/div/div[2]'))).text
    except:
        try: original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleWrap"]/div[2]/div/div/article'))).text
        except: original = "NULL"
    browser.execute_script("window.stop();")
    return original

def joongang(browser):  # 중앙일보, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='article_body']"))).text
    browser.execute_script("window.stop();")
    return original

def hankyung(browser):  # 한국경제
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articletxt"]'))).text
    browser.execute_script("window.stop();")
    return original

def imbc(browser):   # mbc, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/section[1]/article/div[2]/div[4]'))).text
    browser.execute_script("window.stop();")
    return original

def kbs(browser):  # kbs, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cont_newstext"]'))).text
    browser.execute_script("window.stop();")
    return original

def mk(browser):  # 매일경제, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_body"]/div'))).text
    browser.execute_script("window.stop();")
    return original

def jtbc(browser):  # jtbc
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articlebody"]/div[1]'))).text
    browser.execute_script("window.stop();")
    return original

def sbs(browser):   # sbs, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div'))).text
    browser.execute_script("window.stop();")
    return original

def khan(browser):   # 경향신문
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleBody"]'))).text
    browser.execute_script("window.stop();")
    return original


## TODO!!  ------------------------->
def mt(browser): # 머니투데이 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="textBody"]'))).text
    browser.execute_script("window.stop();")
    return original

def news1(browser): # 뉴스원 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articles_detail"]'))).text
    browser.execute_script("window.stop();")
    return original

def nocutnews(browser): # 노컷뉴스 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pnlContent"]'))).text
    browser.execute_script("window.stop();")
    return original

def newsis(browser): # 뉴시스 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[3]/article'))).text
    browser.execute_script("window.stop();")
    return original

def seoul(browser): # 서울신문 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="atic_txt1"]'))).text
    browser.execute_script("window.stop();")
    return original

def ytn(browser): # YTN # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CmAdContent"]/span'))).text
    browser.execute_script("window.stop();")
    return original

def sedaily(browser): # 서울경제 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="atic_txt1"]'))).text
    browser.execute_script("window.stop();")
    return original

def segye(browser): # 세계일보 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_txt"]/article'))).text
    browser.execute_script("window.stop();")
    return original


# url 에 해당하는 신문사의 페이지에서 크롤링 진행
def main(url, browser):
    if 'biz.chosun.com' in url: original = chosun(browser)
    elif 'news.chosun.com' in url: original = chosun(browser)
    elif 'www.chosun.com' in url: original = chosun(browser)
    elif 'www.donga.com' in url: original = donga(browser)
    elif 'www.hani.co.kr' in url: original = hani(browser)
    elif 'www.hankookilbo.com' in url: original = hankookilbo(browser)
    elif 'www.joongang.co.kr' in url: original = joongang(browser)
    elif 'www.yna.co.kr' in url: original = yna(browser)
    elif 'imnews.imbc.com' in url: original = imbc(browser)
    elif 'www.hankyung.com' in url: original = hankyung(browser)
    elif 'news.kbs.co.kr' in url: original = kbs(browser)
    elif 'www.mk.co.kr' in url: original = mk(browser)
    elif 'news.sbs.co.kr' in url: original = sbs(browser)
    elif 'news.jtbc' in url: original = jtbc(browser)
    elif 'news.khan.co.kr' in url: original = khan(browser)
    elif 'news.mt.co.kr' in url: original = mt(browser)
    elif 'newsis.com' in url: original = newsis(browser)
    elif 'www.news1.kr' in url: original = news1(browser)
    elif 'www.nocutnews.co.kr' in url: original = nocutnews(browser)
    elif 'www.seoul.co.kr' in url: original = seoul(browser)
    elif 'www.ytn.co.kr' in url: original = ytn(browser)
    elif 'www.sedaily.com' in url: original = sedaily(browser)
    elif 'www.segye.com' in url: original = segye(browser)
    else: original = 'NULL'
    
    return original


options = webdriver.ChromeOptions()
options.headless=True
options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
browser = webdriver.Chrome('D:\\project\\python_workspace\\chromedriver.exe', options=options)

url = 'https://www.segye.com/newsView/20210825514048'
browser.get(url)


original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_txt"]/article'))).text
browser.execute_script("window.stop();")

print(original)