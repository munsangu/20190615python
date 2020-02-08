for i in range(4): # 4번 반복
    num = int(input("양수 입력: "))
    if num < 0:
        print("입력 오류")
    elif num == 0:
        print("%d는 0입니다."%num)
    elif num % 2 == 0:
        print("%d는 짝수입니다."%num)
    elif num % 2 != 0:
        print("%d는 홀수입니다."%num)
