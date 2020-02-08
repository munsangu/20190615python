#ord() : 문자를 ASCII코드로 변환
#컴퓨터가 문자를 바로 인식하는게 아니라 숫자로 변환하여 인식
#서로 번호로 매치되어있는 사전
print(ord("A"))#65
print(ord("Z"))#90
print(ord("a"))#97
print(ord("z"))#122
for i in "Hello Python":
    print(ord(i),end = " ")
#chr() : ASCII코드를 문자로 변환
print()
print(chr(65))
print(chr(90))
