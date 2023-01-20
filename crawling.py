import urllib.request
from bs4 import BeautifulSoup

# 크롤링할 url 지정
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
# 크롤링한 html
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup)

# 파싱한 html에서 원하는 class가 있는 값만 출력
title = soup.find_all(class_='news_tit')

# print(title)

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()
