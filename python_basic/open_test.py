f=open("./python_basic/word.txt","r")

''' 쓰기(w)
for i in range(1,11):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
'''
''' 읽기(readline)
while True:
     line = f.readline()
     if not line: break
     print(line)
'''
'''읽기(readlines)
lines = f.readlines()
for line in lines:
    print(line)
 '''  








f.close()