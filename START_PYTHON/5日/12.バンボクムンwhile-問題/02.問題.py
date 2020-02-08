import random
Lotte_sum, SL_sum = 0,0 # 롯데, 삼성의 합계 점수
count=1
while True:
    Lotte, SL = random.randint(0,1), random.randint(0,1)
    Lotte_sum += Lotte
    SL_sum += SL
    print(count,"회 롯데 : 삼성 %d:%d"%(Lotte,SL))
    if count > 9:
        if Lotte_sum > SL_sum:
            print("[%d: %d] 롯데가 이겼습니다."%(Lotte_sum,SL_sum))
            break
        elif SL_sum > Lotte_sum:
            print("[%d: %d] 삼성이 이겼습니다."%(Lotte_sum,SL_sum))
            break
        elif count == 12:
            print("연장 12회 동점입니다.")
    count+=1

<정답>
# import random
# Round = 1
# LotteSum, SamsungSum = 0,0 #롯데, 삼성의 합계점수
# while Round <= 12: #Round는 12까지만 반복을 할거야
#     Lotte, Samsung = random.randint(0,1), random.randint(0,1)
#     print("%d Round) L : %d, S : %d"%(Round,Lotte,Samsung))
#     LotteSum += Lotte
#     SamsungSum += Samsung
#     if Round >= 9 and LotteSum != SamsungSum:
#         break
#     Round+=1
# if LotteSum > SamsungSum:
#     print("[%d : %d] 롯데가 승리"%(LotteSum,SamsungSum))
# elif LotteSum < SamsungSum:
#     print("[%d : %d] 삼성이 승리"%(LotteSum,SamsungSum))
# else:
#     print("[%d : %d] 무승부"%(LotteSum,SamsungSum))
