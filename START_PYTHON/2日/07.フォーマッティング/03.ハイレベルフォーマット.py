#방금 배운 포맷코드 => c언어, 자바에서 똑같이 사용
#고급포매팅 => 파이썬에서만 사용
print("I have a {0}".format("Pen"))

print("""I have a {0}, I have a Apple,
Apple{0},
I have a {0}, I have a PineApple,
PineApple{0}""".format("pen"))

print("\n===고급포매팅 변수이용===")
#{숫자} : format()안의 변수의 인덱스
a = "Pen"
b = "Apple"
print("""I have a {0}, I have a {1},
{1}{0},
I have a {0}, I have a Pine{1},
Pine{1}{0}""".format(a,b))

print("\n===고급포매팅 이름이용===")
print("I ate {number} cakes, so i was sick for {day}days".format(number = 10, day =3))

print("I ate {0} cakes, so i was sick for {day}days".format(10, day =3))

#{}안에 아무것도 안적었어 => 포맷코드처럼 순서대로 들어갑니다.
print("I ate {} cakes, so i was sick for {} days".format(10,3))
