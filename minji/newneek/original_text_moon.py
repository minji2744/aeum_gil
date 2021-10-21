import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def chosun(browser):  # 조선일보, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "article-body")))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def donga(browser):  # 동아일보, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[1]')))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text
    
def hani(browser):  # 한겨레신문, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='a-left-scroll-in']/div[2]/div/div[2]")))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def hankookilbo(browser):  # 한국일보, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div[1]")))
    browser.execute_script("window.stop();")

    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def yna(browser):  # 연합뉴스, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleWrap"]/div[2]/div/div/article')))
    browser.execute_script("window.stop();")

    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def joongang(browser):  # 중앙일보, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='article_body']")))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def hankyung(browser):  # 한국경제, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articletxt"]')))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def imbc(browser):   # mbc, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/section[1]/article/div[2]/div[4]')))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def kbs(browser):  # kbs, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cont_newstext"]')))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def mk(browser):  # 매일경제, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_body"]/div')))
    browser.execute_script("window.stop();")
    
    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def jtbc(browser):  # jtbc, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articlebody"]/div[1]')))
    browser.execute_script("window.stop();")

    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    # [앵커] 부분 제거
    word = '[기자]'
    original_text = original_text[original_text.find(word)+len(word):]

    # [김한수 / 서울우유협동조합 팀장 : ~~] 등 인터뷰한 내용은 모두 [~~] 형태로 저장됨
    # ※ 모든 [~~] 형태의 내용이 없어지지만 기사 원문에는 크게 지장이 없을 것 같아 적용
    original_text = re.sub('\[.*\]|\s-\s.*', '', original_text) # [~~] 형태의 모든 데이터 제거

    return original_text

def sbs(browser):   # sbs, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div')))
    browser.execute_script("window.stop();")

    del_tag(browser, original) # 태그 삭제
    
    original_text = original.text
    return original_text

def khan(browser):   # 경향신문, 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleBody"]')))
    browser.execute_script("window.stop();")

    del_tag(browser, original) # 태그 삭제

    original_text = original.text
    return original_text

def mt(browser): # 머니투데이 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="textBody"]')))
    browser.execute_script("window.stop();")

    # 머니투데이 기사는 [@id="textBody"] 밑에 <table>과 <div>를 제거하면 기사만 남는 구조이다.
    # (기사 원문만 가지고 오기 위해서는 해당 태그를 제거)
    del_tag(browser, original) # 태그 삭제

    original_text = original.text
    return original_text

def news1(browser): # 뉴스원 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articles_detail"]')))
    browser.execute_script("window.stop();")

    del_tag(browser, original)

    # 뉴스원 기사는 마지막에 작성한 기자의 이메일 정보가 들어가 있음(태그 안에 있는 것이 아닌 그냥 텍스트로 되어있어서 따로 지워주는 작업 추가)
    original_text = original.text
    # original_text = re.sub('[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', '', original_text) # email 제거
    return original_text

def nocutnews(browser): # 노컷뉴스 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pnlContent"]')))
    browser.execute_script("window.stop();")

    del_tag(browser, original) # 태그 삭제

    original_text = original.text
    return original_text

def newsis(browser): # 뉴시스 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[3]/article')))
    browser.execute_script("window.stop();")

    del_tag(browser, original)

    # 뉴시스 기사는 처음에 '[세종=뉴시스] 김진욱 기자 = ' 문장이 있고,
    # 기사 마지막에는 '◎공감언론 뉴시스' 문장이 있기 때문에 해당 문장을 제거해주는 작업 추가
    original_text = original.text
    # word = ' = '
    # original_text = original_text[original_text.find(word)+len(word):] # (해당 문장이 시작하는 index + 문장의 index) 부터 데이터를 가지고옴
    # word = '◎'
    # original_text = original_text[:original_text.find(word)] # 해당 문장이 시작하는 index 앞 까지만 데이터를 가지고옴
    return original_text

def seoul(browser): # 서울신문 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="atic_txt1"]')))
    browser.execute_script("window.stop();")

    del_tag(browser, original)

    # 서울신문의 경우, '세종 하종훈 기자 artg@seoul.co.kr'라는 문장이 마지막 문단에 들어가있음 // 이 부분 제거
    original_text = original.text
    # original_text = re.sub('[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', '', original_text) # 기자의 이메일 찾아서 제거
    # ot_list = original_text.split('.') # 기사의 마지막이 .으로 끝난다고 가정해서 split해준 다음
    # original_text = original_text[:original_text.find(ot_list[-1])] # 마지막에 들어가있는 기자 정보 제거
    return original_text

def ytn(browser): # YTN # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CmAdContent"]/span')))
    browser.execute_script("window.stop();")

    del_tag(browser, original)

    # ytn의 경우, [앵커]와 [기자]탭으로 분류되어 있다.
    original_text = original.text
    # original_text = re.sub('[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '', original_text) # email 제거

    # [앵커] 부분 제거
    word = '[기자]'
    original_text = original_text[original_text.find(word)+len(word):]

    # [김한수 / 서울우유협동조합 팀장 : ~~] 등 인터뷰한 내용은 모두 [~~] 형태로 저장됨
    # ※ 모든 [~~] 형태의 내용이 없어지지만 기사 원문에는 크게 지장이 없을 것 같아 적용
    original_text = re.sub('\[.*\]|\s-\s.*', '', original_text) # [~~] 형태의 모든 데이터 제거
    # ot_list = original_text.split('.') # .으로 split한 후

    # original_text = original_text[:original_text.find(ot_list[-2])] # 마지막 기자 소개 부분(2문단으로 이루어짐) 빼고 출력
    return original_text

def sedaily(browser): # 서울경제 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="v-left-scroll-in"]/div[2]/div[1]/div[2]')))
    browser.execute_script("window.stop();")

    del_tag(browser, original)

    original_text = original.text
    # email 제거
    # email = re.search('[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', original_text)
    # if email:
    #     original_text = re.sub('[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '', original_text)
    
    # ot_list = original_text.split('.') # .으로 split한 후
    # original_text = original_text[:original_text.find(ot_list[-2])] # 마지막 기자 소개 부분 빼고 출력
    return original_text

def segye(browser): # 세계일보 # 확인
    original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="article_txt"]/article')))
    browser.execute_script("window.stop();")

    del_tag(browser, original)

    original_text = original.text
    # original_text = re.sub('\[.*\]|\s-\s.*', '', original_text) # [~~] 형태의 모든 데이터 제거
    return original_text


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

# <div> 태그 삭제
def del_div(browser, original):
    try:
        div_list = original.find_elements_by_tag_name('div')
        for div in div_list:
            browser.execute_script("arguments[0].remove()", div)
    except:
        pass
# <table> 태그 삭제
def del_table(browser, original):
    try:
        table_list = original.find_elements_by_tag_name('table')
        for table in table_list:
            browser.execute_script("arguments[0].remove()", table)
    except:
        pass

# <span> 태그 삭제
def del_span(browser, original):
    try:
        span_list = original.find_elements_by_tag_name('span')
        for span in span_list:
            browser.execute_script("arguments[0].remove()", span)
    except:
        pass

# <em> 태그 삭제
def del_em(browser, original):
    try:
        em_list = original.find_elements_by_tag_name('em')
        for em in em_list:
            browser.execute_script("arguments[0].remove()", em)
    except:
        pass

# <script> 태그 삭제
def del_script(browser, original):
    try:
        script_list = original.find_elements_by_tag_name('script')
        for script in script_list:
            browser.execute_script("arguments[0].remove()", script)
    except:
        pass

# <figure> 태그 삭제
def del_figure(browser, original):
    try:
        figure_list = original.find_elements_by_tag_name('figure')
        for figure in figure_list:
            browser.execute_script("arguments[0].remove()", figure)
    except:
        pass

# 태그 삭제
def del_tag(browser, original):
    del_div(browser, original)      # <div> 태그 삭제
    del_table(browser, original)    # <table> 태그 삭제
    del_span(browser, original)     # <span> 태그 삭제
    del_script(browser, original)   # <script> 태그 삭제
    del_em(browser, original)       # <em> 태그 삭제
    del_figure(browser, original)   # <figure> 태그 삭제


# options = webdriver.ChromeOptions()
# options.headless=True # 브라우저 띄우지 않고 크롤링 실행
# options.add_argument("--log-level=3") # Chrome Browser의 최소 로그 수준을 설정(INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3)
# options.add_argument('--disable-logging') # 로그를 남기지 않는 옵션
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36") # header 적용
# browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# url = 'http://news.khan.co.kr/kh_news/khan_art_view.html?artid=201901252134015&code=970201'
# browser.get(url)




# # 크롤링
# original = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="articleBody"]')))
# browser.execute_script("window.stop();")

# del_tag(browser, original)

# original_text = original.text


# print(original_text)