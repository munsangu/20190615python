#w는 write => 없는 문서는 만들어줄거야
#이미 있는 문서는 덮어씌어줘요
f = open("new.txt","w")
f.write("파일입력")
f.close()
#열고나선 닫아줘야합니다.
f = open("new.txt","w")
f.write("송진우")
f.close()

f = open("C:\\공유폴더\\10월 평일 12시30분 파이썬\\16일\\17.파일입출력\\student.txt","w")

for i in range(1, 5 + 1):
    name = input("%d번째 학생이름 입력 : "%i)
    data = "%d번째 : %s\n"%(i,name)
    f.write(data)
f.close()

print("\n===with로 파일 출력===")
#with는 자동으로 close 닫아줍니다.
with open("C:\\공유폴더\\10월 평일 12시30분 파이썬\\16일\\17.파일입출력\\student.txt","w") as f:
    for i in range(1, 5 + 1):
        name = input("%d번째 학생이름 입력 : "%i)
        data = "%d번째 : %s\n"%(i,name)
        f.write(data)
