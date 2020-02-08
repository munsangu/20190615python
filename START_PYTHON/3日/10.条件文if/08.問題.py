num1 = 5
num2 = 7
a = int(input("층 입력:"))

# abs() : 절대값 함수
num1 = abs(a - num1)
num2 = abs(a - num2)

# if num1 < 0:
#     num = -num1
# if num2 < 0:
#     num2 = -num2

if num1 < num2:
    print("A 엘리베이터가 움직입니다.")
else:
    print("B 엘리베이터가 움직입니다.")
