import urllib.request, db
from bs4 import BeautifulSoup
import pymysql

params = urllib.parse.urlencode({'page':1})
url = 'https://movie.naver.com/movie/point/af/list.nhn?&%s'%params
print(url)

response = urllib.request.urlopen(url)
navigator=BeautifulSoup(response,'html.parser')
table = navigator.find('table', class_='list_netizen')
print(table)

list_records=[]
for i,r in enumerate(table.find_all('tr')):
    for j,c in enumerate(r.find_all('td')):
        if j == 0:
            record=int(c.text.strip())
        elif j == 2:
            record1=int(c.text.strip())
        elif j == 3:
            record2=str(c.find("a",class_='movie').text.strip())
            record3=str(c.text).split('\n')[2]
        elif j == 4:
            record4=str(c.find("a",class_='author').text.strip())
            record5=str(c.text).split('****')[1]
    try:
        record_t=tuple([record,record1,record2,record3,record4,record5])
        list_records.append(record_t)
    except:
        pass

print(list_records)

conn = db.conn_db()
db.create_table()
db.insert_movie(list_records)