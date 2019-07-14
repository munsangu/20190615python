import pymysql

conn = pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

c = conn.cursor()

# Create table
c.execute('''create table if not exists stocks
        (data text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("insert into stocks values('2006-01-05','BUY','RHAT',100,35.14)")

conn.commit()
conn.close()
