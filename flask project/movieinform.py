import urllib.request
from bs4 import BeautifulSoup
import csv

params = urllib.parse.urlencode({'code':169637})
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?&%s'%params
print(url)

response = urllib.request.urlopen(url)
navigator=BeautifulSoup(response,'html.parser')
table = navigator.find('div', class_='mv_info')
print(table)

list_records=[]

with open('movie2.csv', 'w', newline='',encoding='utf-8') as csvfile:
    fieldnames = ['개요', '감독','출연','등급','흥행']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter='|')
    writer.writeheader()
#     for i,r in enumerate(table.find_all('dl')):
#         for j,c in enumerate(r.find_all('dt')):
#             if j == 0:
#                 record={'개요':str(c.find('dt',class_='step1').text.strip())}
#             elif j == 2:
#                 record.update({'감독':str(c.find('dt',class_='step2').text.strip())})
#             elif j == 3:
#                 record.update({'출연':str(c.find('dt',class_='step3').text.strip())})
#                 record.update({'등급':str(c.find('dt',class_='step4').text.strip())})
#             elif j == 4:
#                 record.update({'흥행':c.find('dt',class_='step9').text.strip()})
#         try:
#             list_records.append(record)
#             # writer.writerow(record)
#         except:
#             pass
#     writer.writerows(list_records)
# print(list_records)

