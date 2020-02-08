#매개변수, 반환값 => 4가지 경우의 수

#매개변수도 있고 반환값도 있는 경우
#매개변수가 있어 : 외부에서 계산할 데이터를 넣어줍니다.
#반환값이 있어 : 계산한 값을 호출했던 곳으로 되돌려줄거야(출력, 저장)
#어딘가저장 = input("뭔가 먹여주죠")
def avg(a, b):
    return (a + b) / 2

x, y = int(input("정수1 : ")), int(input("정수2 : "))
print("평균 : %.2f"%avg(x, y))

#반환값이 없다 : 계산의 결과값을 내부에서 처리를 해야되
#print("뭔가 먹여줘")
def avg(a, b):
    print("평균 : %.2f"%((a + b) / 2))

x, y = int(input("정수1 : ")), int(input("정수2 : "))
avg(x, y)

#매개변수가 없다 : 내부에서 계산할 값을 입력받아야겠네(혹은 계산할 값이 필요없음)
def avg():
    x, y = int(input("정수1 : ")), int(input("정수2 : "))
    return (x + y) / 2

print("평균 : %.2f"%avg())

#둘 다 없어요
def avg():
    x, y = int(input("정수1 : ")), int(input("정수2 : "))
    result = (x + y) / 2
    print("평균 : %.2f"%result)
avg()
