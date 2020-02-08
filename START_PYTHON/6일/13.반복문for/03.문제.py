print("\n=====문제 1번 ======")
sumlist = []
result = 0
while True:
    num = int(input("숫자 입력(0을 입력시 종료): "))
    if num == 0:
        break
    sumlist.append(num)
for i in sumlist:
    print(i)
    result += i
print("합계 : %d"%result)
