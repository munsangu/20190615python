import pymysql

def conn_db():
    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    return conn
conn_db()

# 테이블 생성 함수
def create_table():
    conn=conn_db()
    c = conn.cursor()
    # my_books 테이블 생성(제목, 출판일자, 출판사, 페이지수, 추천여부)
    c.execute('''create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer
        )''')
    conn.commit()
    conn.close()
create_table()

# 데이터 입력 함수
def insert_books():
    conn=conn_db()
    c=conn.cursor()
    # 데이터 입력 방법1
    c.execute("insert into books values('jave','2019-05-20','길벗',500,10)")
    # 데이터 입력 방법2
    sql='insert into books values(%s,%s,%s,%s,%s)'
    c.execute(sql,('Python','2011-02-02','한빛',584,20))
    # 데이터 입력 방법3
    items=[
        ('빅데이터','2014-07-02','삼성',296,11),
        ('안드로이드','2010-02-02','삼성',526,20),
        ('spring','2013-12-02','삼성',248,15)
    ]
    c.executemany(sql,items)
    conn.commit()
    conn.close()
insert_books()

# 전체 데이터 출력 함수
def all_books():
    conn=conn_db()
    c=conn.cursor()
    c.execute("select * from books")

    print('[1] 전체 데이터 출력하기')

    books=c.fetchall()
    print(type(books))
    print(len(books)) # 레코드 개수 출력
    print(books)

    for book in books:
        for i in book:
            print(book[i],end=" ")
        print()
    conn.close()
all_books()