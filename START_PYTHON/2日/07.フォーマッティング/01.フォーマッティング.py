#c언어의 서식문자
#"" 내부에 공간을 비워둠 => 코드를 적을 때 결정이 되는게 아니라
# 출력할 때 결정
a = "현재 통장의 잔고는 %d억원 입니다."
print(a%17)
print(a%100)
print(a%23)

#%d : 정수(decimal)
print("I eat %d cakes"%3)
#%s : 문자열(string)
print("I eat %s cakes"%"two")
#%f : 실수(float)
print("I eat %f cakes"%3.5)

#파이썬 개발자가 => 자료형에 구애를 받네 => %s로 다 받아먹자!
#자료형이 뭔지 모르겠다, 또는 자료형이 아직 결정안됬다 => %s로 받아먹자
print("I eat %s cakes"%3)
print("I eat %s cakes"%3.5)
print("I drink %s Beer"%7.1)
