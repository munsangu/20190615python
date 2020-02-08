print("===문제1===")
num1 = int(input("정수 입력 : "))
if num1 % 5 == 0:
    print("%d는 5의 배수입니다."%num1)
else:
    print("%d는 5의 배수가 아닙니다."%num1)

print("===문제2===")
num1 = int(input("정수 입력 : "))
if num1 % 2 == 0:
    print("%d는 짝수입니다."%num1)
else:
    print("%d는 홀수입니다."%num1)

print("===문제3===")
#언패킹 : 패킹(짐을 싸다) 언패킹(짐을 풀다)
num1,num2 = int(input("첫 번째 수 : ")),int(input("두 번째 수 : "))
if num1 % num2 == 0:
    print("%d는 %d의 배수입니다."%(num1,num2))
else:
    print("%d는 %d의 배수가 아닙니다."%(num1,num2))

print("===문제4===")
#언패킹
num1,num2 = int(input("첫 번째 수 : ")),int(input("두 번째 수 : "))
if num1 > num2:
    if num1 % 2 ==0:
        print("%d은 %d보다 크고 2의배수입니다."%(num1,num2))
if num2 > num1 and num2 % 2 == 0:
    print("%d은 %d보다 크고 2의배수입니다."%(num2,num1))

print("===문제5===")
#언패킹
num1,num2 = int(input("첫 번째 수 : ")),int(input("두 번째 수 : "))
sum = num1 + num2 #변수에 저장하는경우 : 밑에서 여러번 쓰고싶어요
if sum % 2 == 0 and sum % 3 == 0:
    print("%d는 2의배수이고 3의배수입니다."%sum)

print("===문제6===")
num1 = int(input("정수 입력 : "))
#num * -1 : 부호 반전
#-num : 부호 반전
if num1 < 0:
    print("%d의 절대값은 %d입니다."%(num1, -num1))
else:
    print("%d의 절대값은 %d입니다."%(num1, num1))
