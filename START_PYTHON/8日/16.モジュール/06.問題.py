import random
import os
r_c_p = ["가위", "바위", "보"]
computer = int() #빈 int자료형
player = int()
input("""
====가위 바위 보====
<enter를 누르면 시작>
""")
while(1):
    #컴퓨터에게 랜덤으로 가위, 바위, 보 중 하나를 들고옵니다.
    computer_select = random.choice(r_c_p)
    player_select = input("[가위, 바위, 보] :")
    if player_select in r_c_p: #가위 바위 보 리스트 없으면 에러 메시지출력
        if player_select == computer_select:
            print("비겼다! 다시")
        elif (player_select == "가위" and computer_select =="바위") or (player_select == "바위" and computer_select == "보") or (player_select == "보" and computer_select == "가위"):
            print("내가 졌어ㅜㅜ")
            computer += 1
        else:
            print("내가 이겼어!!")
            player += 1

        if computer == 3:
            print("컴퓨터가 이겼습니다.")
            break
        elif player == 3:
            print("※내가 이겼어※")
            break
    else:
        print("잘못 입력했습니다.")
