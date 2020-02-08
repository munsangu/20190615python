import random as r
import time
import os
import turtle as t
#
# t.shape("turtle")
#
# for i in range(50):
#     distance = r.randint(50, 200)
#     angle = r.randint(1, 360)
#     t.fd(distance)
#     t.rt(angle)
# input()

# randnum = r.randint(1,2)
# num = int(input("1, 2중에 선택 : "))
# print("결과는 : ")
# time.sleep(1)
# print("랜덤 값 : %d"%randnum)
# time.sleep(1)
# if randnum == num:
#     print("맞췄습니다.")
# else:
#     print("아깝네요")

# num1 = r.randint(1,9)
# num2 = r.randint(1,9)
# start = time.time() #시작시간 저장
# calc = int(input("%d * %d = "%(num1, num2)))
# end = time.time()
# if calc == num1 * num2:
#     if end - start < 2:
#         print("천재!!")
#     else:
#         print("보통")
# else:
#     print("바보ㅜ")

doll = ["피카츄","라이츄","파이리","꼬북이"]
while(doll): #리스트가 빈 리스트(False)가 되기 전까지 반복
    input("""
    ===== 인 형 뽑 기 =====
    <Enter 누를 시 게임 시작>
    """)
    print("**인형목록**")
    print(doll)
    crain = int(input("숫자를 입력하세요(1 ~ 3) : "))
    answer = r.randint(1, 3)
    if crain == answer:
        select = r.choice(doll)
        print("윙~")
        time.sleep(1)
        print("윙~")
        time.sleep(1)
        print("딸깡~")
        time.sleep(1)
        print("%s가 뽑혔습니다."%select)
        doll.remove(select)
    else:
        print("크레인기계가 이상하게 움직여ㅜㅜ")
    os.system("pause")
    os.system("cls")
print("☆☆인형을 모두 뽑았습니다.☆☆")
