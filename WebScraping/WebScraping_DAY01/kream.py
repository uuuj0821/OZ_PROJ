import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

# 돋보기 누르기
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()

# 검색어 입력 후 엔터
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(30):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.7)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner") # list 형태로 담겨요

product_list = list()

for item in items:
    product_name = item.select_one(".translated_name").text
   
    # 제품명에 후드만 들어간 상품만 출력
    if  "후드" in product_name:
        category = "상의"
        product_brand = item.select_one(".product_info_brand.brand").text
        product_price = item.select_one(".text-lookup.bold.display_paragraph.line_break_by_truncating_tail").text

        product = [category, product_brand, product_name, product_price]
        product_list.append(product)

        # list 형태로 담고 싶은데 [["상의", "슈프림", "티니핑 콜라보 후드", 32030300"], ["상의", "슈프림", "티니핑 콜라보 후드", 32030300"], ...]
        print(f'카테고리 : {category}')
        print(f'브랜드 : {product_brand}')
        print(f'제품명 : {product_name}')
        print(f'가격 : {product_price}')        
        print()

driver.quit()

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0701',
    db = 'kream',
    charset = 'utf8mb4'
)

connection.cursor()

def excute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ()) # 쿼리문을 담아서 데이터베이스에 보냄

        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall() # 접속한 db에 모든 정보 가져오고
        else:
            connection.commit() # 너가 반영하거 저장시켜

for i in product_list:
    excute_query(connection, "INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0], i[1], i[2], i[3]))