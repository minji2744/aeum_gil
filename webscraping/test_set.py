from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re
from original_text import hani # newneek 패키지의 모듈 임포트

def main():
    # csv 파일 만들기
    f = open('test.csv', "w", encoding='utf-8-sig', newline="")
    writer = csv.writer(f)
    col_name = ["original_text"] # column 에 대한 설명 첫행에 추가
    writer.writerow(col_name)
    
    # webdriver option 설정
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars --disable-extensions --no-sandbox --disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"

    for i in range(1,6):
        # webdriver 열기
        driver = webdriver.Chrome(desired_capabilities=caps, options=options)   # selenium driver 크롬
        url = f"https://www.hani.co.kr/arti/list{i}.html"
        driver.get(url)
        time.sleep(5)

        # 기사 element 찾기
        elems = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "article-title [href]")))
        links = [elem.get_attribute('href') for elem in elems]
        print(links)
        driver.quit()

        for link in links:
            driver = webdriver.Chrome(desired_capabilities=caps, options=options)   # selenium driver 크롬
            driver.get(link)
            original = hani(driver)
            original = re.sub(r'[\n\r\t]',' ', original)
            data=[original]
            writer.writerow(data)
            driver.quit()

if __name__ == "__main__":
    main()