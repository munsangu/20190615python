# 함수 : 함수이름() => 이름에 저장되어 있는 코드(기능)이 실행
# a는 문자열 변수 => 내장되어 있는 함수가 많다
print("===문자 개수 세기===")
# 문자열변수, count("찾고 싶은 문자열") : 몇 개가 있는지 찾아줌
a = "happy"
print(a.count("p"))
print(a.count("b"))

print("\n===위치 알려주기1===")
# 문자열 변수, find("문자") => 문자열 변수내의 문자의 인덱스번호를 반환
a = "Python is best choice"
print(a.find("b"))
print(a.find("k")) # 없으면 -1을 반환

print("\n===위치 알려주기2===")
# 문자열변수,index("문자")
print(a.index("b"))
# print(a.index("k")) 없으면 에러메시지 출력

print("\n===문자열 삽입===")
a = "★"
print(a.join("가나다라마바사"))

print("\n===대문자 변환===")
#uppercase : 대문자
a = "hi!"
A = a.upper()
print(A)

print("\n===소문자 변환")
#Lowercase : 소문자
A = "HI!"
a = A.lower()
print(a)

print("\n===왼쪽 공백 지우기 ===")
#Lstrip()
a = "                                              hi!"
print(a.lstrip())

print("\n===오른쪽 공백 지우기===")
a = "hi!                                  "
print(a.rstrip()+"오른쪽")

print("\n===양쪽 공백지우기===")
a = "                           hi!                      "
print("왼쪽" + a.strip() + "오른쪽")

print("\n===문자열 교체===")
a = "Life is too short"
print(a.replace("Life", "Your leg"))

print("\n===문자열 분리===")
a = "Life is too short"
print(a.split()) #split(): 공백을 기준으로 나눠줌 => 리스트로 담아줍니다.
a = "다이제, 메로나, 밀키스, 마이구미"
print(a.split(",")) #split("문자"): 문자를 기준으로 나눠줌

print("\n===문자열 정렬===")
a = "Life is too short"
#()안의 숫자만큼 공간을 할당하고 중앙, 왼쪽, 오른쪽 정렬
print(a.center(30))
print(a.ljust(30))
print(a.rjust(30))
