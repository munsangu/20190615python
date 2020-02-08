import random
#random.randint(a, b) : a ~ b사이의 랜덤한 숫자를 반환

A, B = 100, 100
print("시작)A점수 : %d, B점수 : %d"%(A,B))
count = 0
round = int(input("주사위를 몇 번 던지시겠습니까? : "))
while count < round:
    count += 1
    Adice, Bdice = random.randint(1, 6), random.randint(1, 6)
    print("%d Round) Adice : %d, Bdice : %d"%(count, Adice, Bdice))
    if Adice > Bdice:
        B -= Adice
    elif Bdice > Adice:
        A -= Bdice
    else:
        print("비겼습니다.")
print("종료) A점수 : %d, B점수 : %d"%(A, B))
