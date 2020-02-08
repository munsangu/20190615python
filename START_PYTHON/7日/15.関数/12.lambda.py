# a와 b를 매개변수로 받고 a+b를 return하는 함수
def SUM1(a,b):
    return a + b
print(SUM1(5,6))

# 함수이름 = lambda 매개변수: 반환값
SUM2 = lambda a,b: a+b
print(SUM2(5,6))

MUL =  lambda a,b: a*b
print(MUL(5,6))

print("\n===== 리스트 내부에 함수선언하기 =====")
funclist = [lambda a,b:a+b, lambda a,b:a*b]
# funclist[0] => 더하기 함수
# funclist[1] => 곱하기 함수
print(funclist[0](3,4))
print(funclist[1](3,4))
