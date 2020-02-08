num = int(input("출력할 별의 행 : "))
for i in range(num):
    for j in range(num-i-1):
        print(" ",end ="")
    for j in range(i+1):
        print("*", end="")
    print()
