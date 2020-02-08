# 더하기 기능을 하는 계산기 제작
# 짝수만 더하는 계산기, 홀수만 더하는 계산기, 3의 배수만 더하는 계산기
# 만약에 계산기 50개 제작

# 계산이 축적될 변수
result = 0 # 짝수
result1 = 0 # 홀수
result2 = 0 # 3의 배수

def adder(num):
    global result
    result += num
    return result
def adder1(num):
    global result1
    result1 += num
    return result1
def adder2(num):
    global result2
    result2 += num
    return result2

print(adder(2))
print(adder(4))
print(adder1(5))
print(adder1(11))
print(adder2(3))
print(adder2(6))
