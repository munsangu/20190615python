# 함수는 코드의 길이가 짧아 유지보수가 편함 => 어디서 오류가 낫는지 찾기 쉬움
# 재사용이 가능

# 함수선언
# 함수 용어는 모두 암기 => c언어, JAVA 전부 용어 동일
def func(x): # def 함수이름(매개변수(parameter)):
    y = x * 2 + 1
    return y # 반환값(함수 호출한 곳으로 되돌아가는 값)

result = func(2) # 함수 호출(인자(argument))
print("func : %d"%result)

# 매개변수의 갯수와 인자값의 갯수가 같아야지 실행이 됨.
def avg(a,b):
    result = (a + b) / 2
    return result

print("평균 : %.2f"%avg(10,20))
print("평균 : %.2f"%avg(3,17))
print("평균 : %.2f"%avg(4,7))

# 2, 3 => 2의 3승이 되는 함수를 만들기
def pow(a,b):
    return a ** b
print("제곱 : %d"%pow(2,3))
