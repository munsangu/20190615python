num = int(input("출력할 수의 행 : "))
for i in range(num):
    for j in range(i): # 처음에는 공백 출력 x
        print(" ",end ="")
    for j in range((num-i)*2-1):
        print("%d"%i, end="")
    print()
