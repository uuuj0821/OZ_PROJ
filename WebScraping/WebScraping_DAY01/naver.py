import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색할 키워드를 입력해주세요 : ")

url = base_url + keyword

req = requests.get(url)
html = req.text

soup = BeautifulSoup(html, "html.parser")

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

