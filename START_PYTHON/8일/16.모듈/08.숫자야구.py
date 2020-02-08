answer_list = []
#정답리스트 만들거에요 => 거기다가 임의의 숫자 세개 넣어둘거에요
#[5, 7, 9]
#123 => 0s 0b
#548 => 1s 0b
#3s가 되면 종료
#몇 회만에 맞췄는가
import random as r
import os

answerlist = []
while len(answerlist) <3:
    #answer = random.sample(range(0,10),3)
    answer = r.randint(0,9)
    if answer not in answerlist:
        answerlist.append(answer)
count = 0
while True:
    mylist = []
    s_count = 0
    b_count = 0
    print(answerlist)
    while len(mylist) < 3:
        my = int(input("0~9까지의 숫자를 입력해주세요(%s/3)"%len(mylist)))
        if my < 0 or my > 9:
            print("0~9 사이의 숫자를 입력해주세요")
            continue
        if my not in mylist:
            mylist.append(my)
        else:
            print("이미 존재하는 숫자입니다")
    count += 1
    for i in range(3):
        if answerlist[i] == mylist[i]:
            s_count += 1
        elif answerlist[i] != mylist[i] and answerlist[i] in mylist:
            b_count += 1
    print("%s스트라이크 %s볼 입니다!!"%(s_count,b_count))
    os.system("pause")
    os.system("cls")
    if s_count == 3:
        print("끝내기 홈런으로 승리하셨습니다~~ %s번만에 맞혔습니다"%count)
        break
    else:
        continue