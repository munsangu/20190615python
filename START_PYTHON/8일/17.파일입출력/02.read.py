f = open("C:\\공유폴더\\10월 평일 12시30분 파이썬\\16일\\17.파일입출력\\student.txt","r")
while True:
    line = f.readline() #파일을 한 줄씩 들고와서 저장합니다.
    if line:
        print(line.strip()) #줄바꿈 문자 제거
    else:
        break
f.close()

f = open("C:\\공유폴더\\10월 평일 12시30분 파이썬\\16일\\17.파일입출력\\new.txt","a")
f.write("\n송동열\n송보민")
f.close()
