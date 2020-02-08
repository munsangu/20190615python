import random as r
import os
minscore = 99999 #최고 점수
while 1:
    computer = r.randint(1, 100)
    print("☆☆☆☆☆UPDOWN게임☆☆☆☆☆")
    print("1. 게임시작\n2. 게임전적\n3. 게임종료")
    select = int(input(">>>"))
    if select == 1: #게임시작
        count = 0
        os.system("cls")
        print("=====게임 시작=====")
        while True:
            player = int(input("숫자 입력 : "))
            count += 1
            os.system("cls")
            if computer > player:
                print("===== U  P =====")
            elif computer < player:
                print("===== DOWN =====")
            else: #computer == player
                print("===== ☆☆☆ =====")
                if count < minscore:
                    minscore = count
                    print("☆☆☆최고기록 갱신☆☆☆")
                else:
                    print("☆☆☆%d회 만에 맞췄습니다.☆☆☆"%count)
                os.system("pause")
                os.system("cls")
                break
    elif select == 2:#게임전적
        if minscore == 99999:
            print("===게임을 하고 와주세요===")
        else:
            print("최고 점수는 %d입니다."%minscore)
        os.system("pause")
        os.system("cls")
    elif select == 3: #게임종료
        print("게임을 종료합니다.")
        exit(0)
    else:
        print("잘못된 입력입니다.")
