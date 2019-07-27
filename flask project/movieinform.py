# import
from bs4 import BeautifulSoup
from urllib.request import urlopen
 
url = urlopen("https://movie.naver.com/movie/running/current.nhn")
bs = BeautifulSoup(url, 'html.parser')
body = bs.body
 
target = body.find(class_="lst_detail_t1")
list = target.find_all('li')
no = 1
for n in range(0, len(list)) :
    print("=================================")
    print("No.",no)
    no += 1
    # 영화 제목
    title = list[n].find(class_="tit").find("a").text
    print("영화 제목 :\t", title)
    # # 영화 사진(이미지 추출 안됨..)
    # pic = list[n].find(class_="thumb").find("a")
    # img_src = img.get("https://movie-phinf.pstatic.net/20190718_5/156341294592540aB6_JPEG/movie_image.jpg?type=m99_141_2")
    # print(img_src)
    # 예매율(숫자 출력이 안됨...)
    reservation = list[n].find(class_="num").find_all("dl")
    print("예매율 :\t", reservation,"%")
    # 개요(태그 내 텍스트만 출력 안됨)
    genre=list[n].find(class_="link_txt").find_all("a")
    print("개요 :\t",genre)
    # 상영시간(태그 내 텍스트로 작성되어 있음)
    runtime=list[n].find(class_="split").text
    print("상영시간 :\t",runtime)
    # 개봉일자(태그 내 텍스트로 작성되어 있음) 
    opentime=list[n].find(class_="split").text
    print("개봉일자 :\t",opentime)   
    # 감독
    try:
        director = list[n].find(class_="info_txt1").find_all("dd")[1].find("span").find_all("a")
        directorList = [director.text.strip() for director in director]
        print("제작 감독 :\t", directorList)
    except IndexError:
        print("제작 감독 :\t 정보 없음")
    # 출연 배우
    try:
        cast = list[n].find(class_="lst_dsc").find("dl", class_="info_txt1").find_all("dd")[2].find(class_="link_txt").find_all("a")
        castList = [cast.text.strip() for cast in cast]
        print("출연 배우 :\t", castList)
    except IndexError:
        print("출연 배우 :\t 정보 없음")