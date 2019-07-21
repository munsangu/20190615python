import pymysql

def conn_db():
    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    return conn

def create_table():
    conn=conn_db()
    c = conn.cursor()
    # movie 테이블 생성(글번호, 평점, 영화제목, 140자평, 글쓴이, 날짜)
    # no integer, grade integer, title text, content text, writer text, date text
    c.execute('''create table if not exists movie(
        no int not null,
        grade int,
        title varchar(255),
        content varchar(300),
        writer varchar(30),
        date varchar(20) 
        )''')
    conn.commit()
    conn.close()

# 전체 데이터 출력 함수
def all_movie():
    conn=conn_db()
    c=conn.cursor()
    c.execute("select * from movie")
    items = c.fetchall()
    conn.close()
    return items

# 데이터 입력 함수
def insert_movie(items):
    conn=conn_db()
    c=conn.cursor()
    sql='insert into movie values(%s,%s,%s,%s,%s,%s)'
    c.executemany(sql,items)
    conn.commit()
    conn.close()

# 따옴표 처리
# def store(title,content):
#     title=title.replace("'","''")
#     title=title.replace('"','\"')
#     content=content.replace("'","''")
#     content=content.replace('"','\"')

#     sql='insert into pages(title,content) values(%s,%s)'
#     c.execute(sql,(title,content))
#     connection.commit()


