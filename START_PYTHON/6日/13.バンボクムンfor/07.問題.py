money = 1
result = 0
for i in range(30): # 30번 반복
    result += money
    money *= 2
print("저금한 금액 : %d"%result)

result = 0
for i in range(30): #0 ~ 29
    result += 2 ** i
print("저금한 금액 : %d"%result)
