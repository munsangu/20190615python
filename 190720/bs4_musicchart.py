import urllib.request
from bs4 import BeautifulSoup

url='https://music.bugs.co.kr/chart'
response = urllib.request.urlopen(url)

soup=BeautifulSoup(response, 'html.parser')
results=soup.select('th>p>a') # 필요 정보가 있는 태그를 기록

for result in results:
    print(result.text)
