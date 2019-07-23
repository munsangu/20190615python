from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&tg=0&date=20190721" 

page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
# print(soup)

title_n = soup.find_all('div', class_='tit5')
# 전체 영화의 제목 뽑아옴
movie_name = [soup.find_all('div', 'tit5')[n].a.string for n in range(0, len(title_n))]
# print(movie_name)
# 전체 순위의 평점 뽑아옴
movie_point = [soup.find_all('td', 'point')[n].string for n in range(0, len(title_n))]
# print(movie_point)

movie_dict = {}

for i in range(0, len(title_n)): 
    movie_dict[movie_name[i]] = movie_point[i]

print(movie_dict)