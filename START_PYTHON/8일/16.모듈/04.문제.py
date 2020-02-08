import random as r
import time as t
count = 0#맞춘 횟수
countx = 0#틀린 횟수
start = t.time()
while count < 3:
    num1 = r.randint(1, 9)
    num2 = r.randint(1, 9)
    print("구구단을 외자! 구구단을 외자!")
    calc = int(input("%d * %d = "%(num1,num2)))
    if calc == num1 * num2:
        print("맞췄습니다.")
        count+=1
    else:
        print("틀렸습니다.")
        countx += 1
    print()#엔터키
end = t.time()
print("걸린시간 : %.2f"%(end - start))
print("맞춘 횟수 : %d, 틀린 횟수 : %d"%(count,countx))
