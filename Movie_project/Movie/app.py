from flask import Flask,request,render_template,redirect,jsonify
import pymysql,os
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver as wd
import time,re
# 映画コード入り
import sys
import urllib.request,json, time
import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import LRNounExtractor
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

tmrvl=[]
url="https://movie.naver.com/movie/running/current.nhn"
response = urllib.request.urlopen(url)
soup=BeautifulSoup(response,'html.parser')
table=soup.select('dt.tit a')
for result3 in table:
        mtitle=str(result3.string)
        mcode=str(result3.attrs['href'])
        i = str(re.findall('\d+', mcode)[0])
        tmcode=tuple([i])
        tmtitle=tuple([mtitle])
        tmrvl.append(tmtitle+tmcode)
conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
c=conn.cursor()
# Maria dbに入れる時には??ではなく%sで書く。
sql="INSERT IGNORE INTO test(title,codem) VALUES(%s,%s)"
c.executemany(sql, tmrvl)
conn.commit()
conn.close()
#-------

app=Flask(__name__) #初期化してappアドレス入力

# メーン画面
@app.route('/moviemain') #住所
def mainmovie():
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql="select * from current_movie" 
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        conn.close()
    return render_template('main.html',movieList=result)

# 上映予定の映画
@app.route('/Future_movie')
def to_be_movie():
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)    
    try:
        with conn.cursor() as cursor:
            sql="select * from movie_to_be_screened" 
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        conn.close()
    return render_template('Future_movie.html',to_be_movieList=result)

# ajax検索
@app.route('/ajaxmain',methods=['POST'])# 住所
def searchmovie():
    text=request.form.get('text')
    stype=request.form.get('stype')
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            if stype == 'current_movie_open':
                sql='select * from current_movie where current_movie_open like %s'
                text='%'+text+'%'
                cursor.execute(sql,text)
                movieList=cursor.fetchall()# 全部持って来る時
                print(movieList)
                
            elif stype == 'current_movie_genre':
                sql='select * from current_movie where current_movie_genre like %s'
                text='%'+text+'%'
                cursor.execute(sql,text)
                movieList=cursor.fetchall()# 全部持って来る時
                print(movieList)
            else:
                sql='select * from current_movie where current_movie_title like %s'
                text='%'+text+'%'
                cursor.execute(sql,text)
                movieList=cursor.fetchall()# 全部持って来る時
                print(movieList)
    finally:
        conn.close()
        return jsonify(movieList)

#映画詳細
@app.route('/movie_detail/<m_no>/<current_movie_title>')#住所
def detail(m_no,current_movie_title):    
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='select * from current_movie c inner join test t on c.current_movie_title = t.title where current_movie_title = %s;'
            cursor.execute(sql,(current_movie_title))
            result=cursor.fetchone() #一つだけ持って来る時

            sql='select * from current_movie where current_movie_title = %s;'
            cursor.execute(sql,(current_movie_title))
            result1=cursor.fetchone() #一つだけ持って来る時

            sql='select * from board where m_no= %s;'
            cursor.execute(sql,(m_no))
            board=cursor.fetchall()
    finally:
        conn.close()
    if result is not None:    
        tmrvl=[]
        movieName = result['codem']

        for page in range(1,200):
            url="https://movie.naver.com/movie/bi/mi/review.nhn?code="+str(movieName)+"&page="+str(page)
            response = urllib.request.urlopen(url)

            soup=BeautifulSoup(response,'html.parser')
            table=soup.select('ul.rvw_list_area li a')
            for result3 in table:
                mrv=str(result3.string)
                tmrv=tuple([mrv])
                tmrvl.append(tmrv)
                #tmrv1=str(tmrv)
                #f.write(tmrv1)
        df=pd.DataFrame(tmrvl)

        def preprocessing(text):
            # 改行文字除去
            text = re.sub('\\\\n', ' ', text)
            return text
        
        tokenizer = RegexTokenizer()
        stopwords_kr = ['하지만', '그리고', '그런데', '저는','제가',
                        '그럼', '이런', '저런', '합니다',
                        '많은', '많이', '정말', '너무','[',']','것으로','했습니다','했다'] 

        sentences = df[0].apply(preprocessing)

        # soynlp로 名詞抽出法
        noun_extractor = LRNounExtractor(verbose=True)
        noun_extractor.train(sentences)
        nouns = noun_extractor.extract()
    
        # イメージファイルの上に出力する
        img = Image.open('Movie_project/Movie/static/img/cloud.png')
        img_array=np.array(img)

        wordcloud = WordCloud( font_path = '/Library/Fonts/NanumBarunGothic.ttf', 
                            stopwords = stopwords_kr,
                            background_color = 'white', 
                            mask=img_array,
                            width = 800, height = 600).generate(' '.join(nouns))
        plt.figure(figsize = (15 , 10))
        plt.imshow(wordcloud)
        plt.axis("off")
        #plt.show()  
        url1="Movie_project/Movie/static/wordcloud/" + current_movie_title + ".png"
        wordcloud.to_file(url1)
    

    return render_template('movie_detail.html', wordInfo=result, board=board, movieInfo=result1)

#上映予定映画詳細
@app.route('/show_movie_detail/<m_no>')#住所
def show_movie_detail(m_no):
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='select * from movie_to_be_screened where m_no= %s;'
            cursor.execute(sql,(m_no))
            result=cursor.fetchone() #一つだけ持って来る時

            sql='select * from board where m_no= %s;'
            cursor.execute(sql,(m_no))
            board=cursor.fetchall()
    finally:
        conn.close()
    return render_template('show_movie_detail.html', movieInfo=result, board=board)

'''#영화등록
@app.route('/form', methods=['GET'])
def formTest():
    return render_template('form.html')#form.html을 호출하겟다
'''
#現在映画登録
@app.route('/')
def formresult():
    
    driver = wd.Chrome(executable_path='Movie_project/Movie/data/chromedriver')

    #映画リストをお持ち帰り

    movie_title = [] #映画のタイトル
    movie_genre = [] #映画年齢
    movie_img = []  #映画のポスター
    movie_img_Processing =[] #영화포스터주소(가공후)
    #movie_score = [] #映画評点
    movie_open = [] #영화오픈날짜
    movie_story = [] #映画のあらすじ

    #ページにある映画のタイトルを出力
    for movie_page in range(1,4):
        #print("https://movie.daum.net/premovie/released?opt=reserve&page=",movie_page)    
        url = "https://movie.daum.net/premovie/released?opt=reserve&page={}".format(movie_page)
        driver.get(url)
        html = driver.page_source

        soup = BeautifulSoup(html,'html.parser')
        
        #映画のタイトル抽出
        movietitles = soup.find_all('a',class_='name_movie #title')
        
        for movietitle in movietitles:
            movie_title.append(movietitle.text)
        
        #映画年齢抽出
        movieGenres = soup.find_all('em',class_='ico_movie')
        
        for movieGenre in movieGenres:
            if movieGenre.text == "독점":
                continue
            else:
                movie_genre.append(movieGenre.text)
        #映画のイメージ抽出
        movieImgs = soup.select("div span img.img_g")
        
        for movieImg in movieImgs:
            movie_img.append(movieImg['src'])
            # time.sleep(3)
        #映画評点抽出
        #movieScores = soup.find_all('span',class_='num_grade')
        #for moiveScore in movieScores:
            #print(moiveScore.text)

        #映画公開日の抽出
        movieOpens = soup.find_all('span',class_='info_state')

        #映画公開日の正規表現を活用して抽出
        for movieOpen in movieOpens:
            movieOpen_cleand = re.sub('[a-zA-Z]' , '', movieOpen.text)
            movieOpen_cleand = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                            '', movieOpen.text)              
            movieOpen_cleand_final = movieOpen_cleand.split()
            movie_open.append(movieOpen_cleand_final[0])
            movieStorys = soup.find_all('a' , class_="desc_movie #synop")
        
        for movieStory in movieStorys:
            movieStory_cleand = movieStory.text.strip()
            movieStroy_cleand_final = movieStory_cleand.replace("\n","")
            movie_story.append(movieStroy_cleand_final)        
    #映画の画像アドレス加工
    for moviesoso in range(len(movie_img)):
        movie_img_Processing.append(movie_img[moviesoso].replace("//img1.daumcdn.net/thumb/C236x340/?fname=","")) 


    #リストの中に映画のタイトルが入っているか確認。
    #print(len(movie_title))

    #リストの中に映画年齢が入っているか確認
    #print(len(movie_genre))

    #リストの中に映画のイメージが入っているか確認。
    #print(movie_img)

    #リストの中に映画の公開日が入っているか確認
    #print(len(movie_open))

    #リストの中にストーリーが入っているか確認。
    #print(len(movie_story))

    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    #データの削除·登録
    try:
        with conn.cursor() as cursor:
            sql="delete from current_movie"
            cursor.execute(sql)
            conn.commit()
            for insert in range(len(movie_title)):    
                sql="insert into current_movie(current_movie_title,current_movie_img,current_movie_genre,current_movie_open,current_movie_story) values(%s,%s,%s,%s,%s);"
                cursor.execute(sql,(movie_title[insert],movie_img_Processing[insert],movie_genre[insert],movie_open[insert],movie_story[insert]))
                conn.commit()
    finally:
        conn.close()

    
    #######上映予定の映画リストをお持ち帰り##############

    Show_movie_title = [] #上映予定映画のタイトル
    #Show_movie_genre = [] #上映予定の映画等級
    Show_movie_img = []  #上映予定の映画ポスター
    Show_movie_img_Processing =[] #上映予定映画のポスターアドレス(架空後)
    #movie_score = [] #上映予定の映画評点
    Show_movie_open = [] #上映予定映画のオープンの日時
    Show_movie_story = [] #上映予定映画のあらすじ

    #ページにある映画のタイトルを出力
    for movie_page in range(1,6):
        #print("https://movie.daum.net/premovie/released?opt=reserve&page=",movie_page)    
        url = "https://movie.daum.net/premovie/scheduled?opt=reserve&page={}".format(movie_page)
        driver.get(url)
        html = driver.page_source

        soup = BeautifulSoup(html,'html.parser')
        
        #映画のタイトル抽出
        movietitles = soup.find_all('a',class_='name_movie #title')
        
        for movietitle in movietitles:
            Show_movie_title.append(movietitle.text)
        
        #映画年齢抽出
        #movieGenres = soup.find_all('em',class_='ico_movie')    
        #for movieGenre in movieGenres:
            #if movieGenre.text == "독점":
                #continue
            #else:
                #Show_movie_genre.append(movieGenre.text)
        
        #映画のイメージ抽出
        movieImgs = soup.select("div span img.img_g")
            
        for movieImg in movieImgs:
            Show_movie_img.append(movieImg['src'])

        #映画評点抽出
        #movieScores = soup.find_all('span',class_='num_grade')
        #for moiveScore in movieScores:
            #print(moiveScore.text)

        #映画公開日の抽出
        movieOpens = soup.find_all('span',class_='info_state')

        #映画公開日の正規表現を活用して抽出
        for movieOpen in movieOpens:
            movieOpen_cleand = re.sub('[a-zA-Z]' , '', movieOpen.text)
            movieOpen_cleand = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                            '', movieOpen.text)              
            movieOpen_cleand_final = movieOpen_cleand.split()
            Show_movie_open.append(movieOpen_cleand_final[0])

        movieStorys = soup.find_all('a' , class_="desc_movie #synop")
        for movieStory in movieStorys:
            movieStory_cleand = movieStory.text.strip()
            movieStroy_cleand_final = movieStory_cleand.replace("\n","")
            Show_movie_story.append(movieStroy_cleand_final)
    driver.close()        
    #映画の画像アドレス加工
    for moviesoso in range(len(Show_movie_img)):
        Show_movie_img_Processing.append(Show_movie_img[moviesoso].replace("//img1.daumcdn.net/thumb/C236x340/?fname=","")) 

    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    #データの削除·登録
    try:
        with conn.cursor() as cursor:
            sql="delete from movie_to_be_screened"
            cursor.execute(sql)
            conn.commit()    
            for insert in range(len(Show_movie_title)):        
                sql="insert into movie_to_be_screened(show_movie_title,show_movie_img,show_movie_open,show_movie_story) values(%s,%s,%s,%s);"
                cursor.execute(sql,(Show_movie_title[insert],Show_movie_img_Processing[insert],Show_movie_open[insert],Show_movie_story[insert]))
                conn.commit()
    finally:
        conn.close()   
    return redirect('/moviemain')
    #リストの中に映画のタイトルが入っているか確認
    #print(Show_movie_title)

    #リストの中に映画年齢が入っているか確認
    #print(Show_movie_genre)

    #リストの中に映画のイメージが入っているか確認。
    #print(Show_movie_img)

    #リストの中に映画の公開日が入っているか確認
    #print(Show_movie_open)

    #リストの中にストーリーが入っているか確認。
    #print(Show_movie_story[0])

    

#映画削除
'''@app.route('/delete_movie/<m_no>',methods=['GET'])
def deleteform(m_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="delete from movie where m_no= %s;"
            cursor.execute(sql,(m_no))
            conn.commit()
    finally:
        conn.close()

        return redirect('/moviemain')'''

#映画内容の修正
'''@app.route('/update_movie/<m_no>',methods=['GET'])
def updateform(m_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="select * from movie where m_no= %s;"
            cursor.execute(sql,(m_no))
            result=cursor.fetchone() #하나만 가져올떄
    finally:
        conn.close()

        return render_template('update_movie.html',list=result)'''
#映画内容の修正
'''@app.route('/update_movie',methods=['POST'])
def updateformp():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    no = request.form.get('no') 
    title = request.form.get('title') 
    mdir = request.form.get('mdir') 
    act = request.form.getlist('act') 
    grade = request.form.getlist('grade') 
    date = request.form.getlist('date') 
    content = request.form.get('content')
    img = request.files['img']
    dirname=os.path.dirname(__file__) + '/static/uploads/'+img.filename

    try:
        with conn.cursor() as cursor:
            sql="update movie set m_title=%s,m_dir=%s,m_act=%s,m_content=%s,m_grade=%s,m_img=%s,m_date=%s where m_no=%s;"
            cursor.execute(sql,(title,mdir,act,content,grade,img.filename,date,no))
            conn.commit()
    finally:
        img.save(dirname)
        conn.close()
    return redirect('/moviemain')'''

#掲示板の書き込み
@app.route('/board_write/<m_no>',methods=['GET'])
def boardW(m_no):
    return render_template('board_write.html',m_no=m_no)#form.html

@app.route('/board_write/<m_no>',methods=['POST'])
def boardP(m_no):
    title = request.form.get('title') 
    writer = request.form.get('writer') 
    content = request.form.get('content') 
    good = request.form.get('good') 
    m_no = request.form.get('m_no') 
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="insert into board(b_title,writer,b_content,good,m_no,b_date) values(%s,%s,%s,%s,%s,SYSDATE());"
            cursor.execute(sql,(title,writer,content,good,m_no))
            conn.commit()
    finally:
        conn.close()
    return redirect('/movie_detail/'+m_no)

#文の内容
@app.route('/board_content/<b_no>',methods=['GET'])
def boardC(b_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='select * from board where b_no = %s' 
            cursor.execute(sql,(b_no))
            result=cursor.fetchone()

    finally:
        conn.close()
    return render_template('board_content.html',list=result)

if __name__=="__main__": #ファイル内でのみダイレクトに動作
    app.run()
#host0.0.0.0は外部でもアクセス可能、portは基本5000に変えたいなら変えればなる