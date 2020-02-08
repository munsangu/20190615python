import time as t

correct1 = "내가 그린 목이긴 기린그림은 잘 그린 기린그림이고"
correct2 = "니가 그린 그린기린그림은 목 그린 기린그림이다"

input("""
문장을 따라 적으세요
<Enter 누를 시 게임시작>
""")
#시작시간 입력
start = t.time()
print(correct1)#1번 문장을 출력
answer1 = input()#1번 문장 입력
print(correct2)#2번 문장을 출력
answer2 = input()#2번 문장 입력
end = t.time()
result = end - start

if answer1 == correct1 and answer2 == correct2:
    print("소요 시간 : %.2f"%result)
else:
    print("틀렸습니다. 다시 도전하세요")
