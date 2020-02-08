f = open("abc.txt","r")
lines = f.readlines() #모든 라인을 읽어옴
f.close()

rlines = reversed(lines) #읽은 라인을 역순으로 정렬

f = open("abc.txt","w")
for line in rlines:
    line = line.strip()
    f.write(line)
    f.write("\n")
f.close()
