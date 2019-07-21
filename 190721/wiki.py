import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
soup = BeautifulSoup(html,'html.parser')

# class가 wikitable인 태그들 주에서 첫번째 태그 선택

table = soup.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

# wt: 텍스트 쓰기 모드
csvFile=open('crawling/editors.csv','wt',newline='',encoding='utf-8')

# csv 파일 저장 객체
write=csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        # td, th 태그의 내용을 리스트에 추가
        for cell in row.find_all(['td','th']):
            csvRow.append(cell.get_text())
        write.writerow(csvRow)
finally:
    print('csv로 저장되었습니다.')
    csvFile.close()