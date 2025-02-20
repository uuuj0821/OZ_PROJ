from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup # 파이썬은 html 코드를 모른다. 그래서 파이썬에게 html 이란 무엇인지 알려주기 위함
import time

header_user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색할 키워드를 입력해주세요 : ")

options_ = Options()
options_.add_argument(f'User-Agent={header_user}') # 유저정보 넣기
options_.add_experimental_option('detach', True) # 자동으로 브라우저가 종료되지 않음
options_.add_experimental_option("excludeSwitches", ["enable-automation"]) #Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다. 라는 상단에 메시지 삭제해줌 // 해당코드는 불필요한 경고창?을 제거해주는 것!

url = base_url + keyword
driver = webdriver.Chrome(options=options_)
driver.get(url)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

html = driver.page_source  # 웹의 소스 다 가져와!
soup = BeautifulSoup(html, "html.parser") # 파이썬에 이것이 바로 html 이란다! 라고 설정해주는 것 // selenium에는 parser가 없음. 그래서 bs4를 같이 사용함
results = soup.select(".view_wrap")

for num, i in enumerate(results, 1):
    title = i.select_one(".title_link").text
    link = i.select_one(".title_link")["href"]
    writer = i.select_one(".name").text
    dsc = i.select_one(".dsc_link").text
    
    print(f'{num}번째 블로그')
    print(f'제목 : {title}')
    print(f'링크 : {link}')
    print(f'작성자 : {writer}')
    print(f'요약 : {dsc}')
    print("")

driver.quit()

'''
정적스크래핑 : 스크롤이 되지 않는 상태에서 스크래핑
동적스크래핑 : 스크롤을 최하단으로 내려서 모든 글을 스크래핑
'''