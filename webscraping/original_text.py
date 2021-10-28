import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def chosun(browser):  # 조선일보, 확인
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "article-body"))).text
        browser.execute_script("window.stop();")
    except: original = 'NULL'
    return original

def donga(browser):  # 동아일보
    try: 
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "article_txt"))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original
    
def hani(browser):  # 한겨레신문, 확인
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='a-left-scroll-in']/div[2]/div/div[2]"))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def hankookilbo(browser):  # 한국일보
    try:
        texts = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "editor-p")))
        browser.execute_script("window.stop();")
        original = ''
        for text in texts:
            original = original + text.text + ' '
    except: 
        try: # /html/body/div[1]/div[1]/div[4]/div/div[1]
            original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div[1]"))).text
            browser.execute_script("window.stop();")
        except: original = "NULL"
    return original

def yna(browser):  # 연합뉴스, 확인 (조금 문제 있음)
    try: original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleWrap"]/div/div[2]'))).text
    except:
        try: original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleWrap"]/div[2]/div/div/article'))).text
        except: original = "NULL"
    browser.execute_script("window.stop();")
    return original

def joongang(browser):  # 중앙일보, 확인
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='article_body']"))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def hankyung(browser):  # 한국경제
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articletxt"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def imbc(browser):   # mbc, 확인 
    try:   
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/section[1]/article/div[2]/div[4]'))).text
        browser.execute_script("window.stop();")
    except: 
        try:   # //*[@id="content"]/div/section[1]/article/div[2]/div[5] 
            original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/section[1]/article/div[2]/div[5]'))).text
            browser.execute_script("window.stop();")
        except: original = "NULL"
    return original

def kbs(browser):  # kbs, 확인
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cont_newstext"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def mk(browser):  # 매일경제, 확인
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_body"]/div'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def jtbc(browser):  # jtbc
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articlebody"]/div[1]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def sbs(browser):   # sbs, 확인
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div'))).text
        browser.execute_script("window.stop();")
    except:
        original = "NULL"
    return original

def khan(browser):   # 경향신문, 문제 있음 잘 못긁어옴, 여전히 문제 있음...
    try:  # //*[@id="articleBody"]
        original = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleBody"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def mt(browser):
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="textBody"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def news1(browser):
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articles_detail"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def nocutnews(browser):
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pnlContent"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def newsis(browser):
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[3]/article'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def seoul(browser):
    try:    
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="atic_txt1"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def ytn(browser):
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CmAdContent"]/span'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def sedaily(browser):
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="v-left-scroll-in"]/div[2]/div[1]/div[2]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def segye(browser):
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_txt"]/article'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def edaily(browser):  # www.edaily.co.kr
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/section[1]/section[1]/div[1]/div[3]/div[1]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def dongascience(browser):  # www.dongascience.com
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_body"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def asiae(browser):  # view.asiae.co.kr
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[3]/div[3]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def voakorea(browser):  # www.voakorea.com
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article-content"]/div'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def huffingtonpost(browser):  # www.huffingtonpost.kr
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/article/div/div[1]/div/div[1]/div'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def naver(browser):  # terms.naver.com
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="size_ct"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

def kmib(browser):  # news.kmib.co.kr
    try:
        original = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleBody"]'))).text
        browser.execute_script("window.stop();")
    except: original = "NULL"
    return original

# ko.wikipedia.org
# zdnet.co.kr
# www.sisain.co.kr
# www.munhwa.com
# www.joongang.co.kr

# url 에 해당하는 신문사의 페이지에서 크롤링 진행
def get_original(url):
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    browser = webdriver.Chrome(desired_capabilities=caps)   # selenium driver 크롬
    browser.get(url)
    time.sleep(4)
    url = browser.current_url   # 현재 url 주소 가져오기

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
    elif 'www.edaily.co.kr' in url: original = edaily(browser)
    elif 'www.dongascience.com' in url: original = dongascience(browser)
    elif 'asiae' in url: original = asiae(browser)
    elif 'voakorea' in url: original = voakorea(browser)
    elif 'huffingtonpost' in url: original = huffingtonpost(browser)
    elif 'terms.naver' in url: original = naver(browser)
    elif 'kmib' in url: original = kmib(browser)
    else: original = 'NULL'
    
    browser.close()
    
    return original, url
