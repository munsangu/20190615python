import sqlite3, csv

input_file = 'input.csv'

conn=sqlite3.connect("suppliers.db")
c=conn.cursor()

file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header=next(file_reader,None)
print(header)

for row in file_reader:
    data=[]
    for idx in range(len(header)):
        data.append(row[idx])
    print(data)
    c.execute('insert into suppliers values(?,?,?,?,?)',data)

conn.commit()