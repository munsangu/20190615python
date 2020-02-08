num = int(input("출력할 별의 행 : "))
for i in range(num): # num만큼 반복 -> 몇 행
    for j in range(i+1): # 한 행에 몇 개의 별을 찍을 것인가?
        print("*", end="")
    print()
