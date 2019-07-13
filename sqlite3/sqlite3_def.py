import sqlite3

#테이블 생성
def create_table():
    conn=sqlite3.connect('my_books.db')
    c=conn.cursor()
   #my_books 테이블 생성(제목, 출판일자, 출잔사, 페이지수, 추천여부)
    c.execute('''create table if not exists books(
        title text, 
        published_date text,
        publisher text,
        pagas integer,
        recommend integer
        )''')
    conn.commit()
    conn.close()


#데이터 입력 함수
def insert_books(items):
    conn=sqlite3.connect('my_books.db') #db연결
    c=conn.cursor()
    #데이터 입력 방법1
    #c.execute("insert into books values('Java','2019-05-20','길벗',500,10)")
    sql='insert into books values(?,?,?,?,?)'
    #데이터 입력 방법2
    #c.execute(sql,('Python','2010-04-20','한빛',584,20))
    #데이터 입력 방법3
    c.executemany(sql,items)
    conn.commit()
    conn.close()


#전체 데이터 출력 함수
def all_books():
    conn=sqlite3.connect('my_books.db')
    c=conn.cursor()
    c.execute("select * from books")
    print("[1] 전체 데이터 출력하기")
    books = c.fetchall()
    print(type(books))
    print(len(books)) #레코드 갯수 출력

    for book in books:
        for i in book:
            print(i, end=" ")
        print()
    conn.close()
