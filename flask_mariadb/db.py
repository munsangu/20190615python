import pymysql

def conn_db():
    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    return conn

# 테이블 생성 함수
def create_table():
    conn=conn_db()
    c = conn.cursor()
    c.execute('''create table if not exists users(
        userid varchar(11) not null,
        email varchar(255) not null,
        address varchar(255),
        password varchar(255) not null,
        PRIMARY KEY (userid)
        )''')
    conn.commit()
    conn.close()

# 데이터 입력 함수
def insert_users(user):
    conn=conn_db()
    c=conn.cursor()
    sql='insert into users values(%s,%s,%s,%s)'
    c.execute(sql,user)
    conn.commit()
    conn.close()

# 전체 데이터 출력 함수
def all_users():
    conn=conn_db()
    c=conn.cursor()
    c.execute("select * from users")
    users = c.fetchall()
    print(len(users))
    print(users)
    conn.close()
    return users

def one_user(userid):
    conn=conn_db()
    c=conn.cursor()
    sql='select * from users where userid=%s'
    c.execute(sql,userid)
    user = c.fetchone()
    conn.commit()
    conn.close()
    return user   
 
# 데이터 삭제 함수
def delete_user(userid):
    conn=conn_db()
    c=conn.cursor()
    sql='delete from users where userid=%s'
    c.execute(sql,userid)
    conn.commit()
    conn.close()

# 데이터 수정 함수
def update_user(user):
    conn=conn_db()
    cursor=conn.cursor()
    print(user)
    sql='''update users 
            set email=%s,
                address=%s,
                password=%s
            where userid=%s
        '''
    cursor.execute(sql,(user['email'],user['address'],user['password'],user['userid']))
    conn.commit()
    conn.close()
    