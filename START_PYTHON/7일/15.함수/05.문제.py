print("\n===== 1번 문제 =====")
def sum(a):
    result = 0
    for i in range(a+1):
        result += i
    return result

x= int(input("정수 :"))
print("누적 합계: %d"%sum(x))

print("\n===== 2번 문제 =====")
def alrpa(num):
    if num % 3 ==0:
        print("3의 배수입니다. ")
    else:
        print("3의 배수가 아닙니다. ")
num = int(input("정수 입력: "))
alrpa(num)

print("\n===== 3번 문제 =====")
def beta():
    x, y = int(input("정수1 :")), int(input("정수2 :"))
    if x > y:
        return x
    elif y > x:
        return y
print(beta())

print("\n===== 4번 문제 =====")
def ceta():
    x = int(input("정수: "))
    if x > 0:
        print(x)
    elif x < 0:
        print(-x)
ceta()

# # ﻿print("===문제1===")
# # def total(a):
# #     sum = 0
# #     for i in range(a + 1):
# #         sum += i
# #     return sum
# # num = int(input("정수 입력 : "))
# # print("1부터 {0}까지의 합계는 : {1}".format(num,total(num)))
#
# # print("\n===문제2===")
# # def ThreeMul(a):
# #     if a % 3 ==0:
# #         print("%d는 3의 배수입니다."%a)
# #     else:
# #         print("%d는 3의 배수가 아닙니다."%a)
# # num = int(input("정수 입력 : "))
# # ThreeMul(num)#함수 호출
#
# print("\n===문제3===")
# def Compare():
#     #map(함수,입력) -> 함수를 여러개의 데이터에 한번에 적용
#     a, b = map(int, input("정수 두 개 입력 : ").split())
#     #map(int, "5 10".split())
#     #map(int, ["5", "10"])
#     #[5, 10]
#     if a >= b:
#         return a
#     else:
#         return b
# print("두 수중에 큰 수는 : %d"%Compare())
#
# print("\n===문제4===")
# def Abs():
#     a = int(input("정수 입력 : "))
#     if a < 0:
#         print("%d의 절대값 : %d"%(a,-a))
#     else:
#         print("%d의 절대값 : %d"%(a,a))
# Abs()
