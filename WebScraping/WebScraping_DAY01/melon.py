import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

# 멜론은 User-Agent 체크를 하기 때문에 헤더 추가
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
req = requests.get(url, headers=headers)
html = req.text
# print(req)
# print(req.status_code)

if req.status_code != 200:
    print("[Error] 페이지를 불러오는 데 실패했습니다.")
else:
    soup = BeautifulSoup(html, "html.parser") 
    lsts = soup.select("[class^=lst]")

    for rank, name in enumerate(lsts, 1):
        song_title = name.select_one(".ellipsis.rank01 a").text
        singer = name.select_one(".ellipsis.rank02 a").text

        print(f'순위 : {rank}')
        print(f'가수 : {singer}')
        print(f'노래제목 : {song_title}\n')



