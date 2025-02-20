from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup # 파이썬은 html 코드를 모른다. 그래서 파이썬에게 html 이란 무엇인지 알려주기 위함
import time

header_user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f'User-Agent={header_user}') # 유저정보 넣기
options_.add_experimental_option('detach', True) # 자동으로 브라우저가 종료되지 않음
options_.add_experimental_option("excludeSwitches", ["enable-automation"]) #Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다. 라는 상단에 메시지 삭제해줌 // 해당코드는 불필요한 경고창?을 제거해주는 것!

driver = webdriver.Chrome(options=options_)

url = "https://kream.co.kr/"
driver.get(url)