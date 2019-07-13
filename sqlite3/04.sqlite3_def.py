import sqlite3

# 테이블 생성
def create_table():
    conn=sqlite3.connect('my_books.db')
    c=conn.cursor()
     # my_books 테이블 생성(제목, 출판일자, 출잔사, 페이지수, 추천여부)
    c.execute('''create table if not exists books(
        title text, 
        published_date text,
        publisher text,
        pagas integer,
        recommend integer
        )''')
    conn.commit()
    conn.close()
create_table()
# 데이터 입력 함수
def insert_books():
    conn=sqlite3.connect('my_books.db')#db변경
    c=conn.cursor()
    # 데이터 입력 방법1
    c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    # 데이터 입력 방법2
    sql='insert into books values(?,?,?,?,?)'
    c.execute(sql,('Python','2010-04-20','한빛',584,20))
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

def all_books():
    conn=sqlite3.connect('my_books.db')
    c=conn.cursor()
    c.execute("select * from books")
    print("[1] 전체 데이터 출력하기")
    books = c.fetchall()
    print(type(books))
    print(len(books))

    for book in books:
        for i in book:
            print(i, end=" ")
        print()
    conn.close()
all_books()