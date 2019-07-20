import urllib.request, time
from bs4 import BeautifulSoup

# 네이버 뉴스 - 속보- 연합뉴스 속보 - 가장 많이 본 뉴스
url ='https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
#results=soup.find_all('a',class_='nclicks(cnt_flashart)')
results=soup.select('.section_list_ranking li a')
print(results)

for result in results:
    print('제목:',result.attrs['title'])
    print('링크:',result.attrs['href'])
    print()
    url_content='https://news.naver.com'+result.attrs['href']
    response_content = urllib.request.urlopen(url_content)
    soup_content = BeautifulSoup(response_content, 'html.parser')
    content=soup_content.select_one('#articleBodyContents')
    # print(content.contents)

# 가공작업
    output=''
    for item in content.contents:
        stripped = str(item).strip() # 공백 제거
        if stripped == '':
            continue
        if stripped[0] not in['<','/']: # 태그나 주석 제거
            output+=str(item).strip()
    output = output.replace('무단 전재 및 재배포 금지','')
    output = output.replace('본문 내용TV플레이어','')
    print(output)
    print()

    time.sleep(3)