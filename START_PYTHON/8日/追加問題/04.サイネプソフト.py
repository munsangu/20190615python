# 1.박씨와 이씨는 각각 몇 명 인가요?
# 2."박주형"이란 이름이 몇 번 반복되나요?
# 3.중복을 제거한 이름을 출력하세요.
# 4.중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
name = "박선호,박주형,우수연,이지우,이지혁,박주형,정의영,유창준,조정은,박주형,강동수,윤정현,박현민,이신주"
name = name.split(",")
print("===1번 문제===")
lastname = []
for i in name:
    lastname.append(i[0])
print("박씨 : %d, 이씨 : %d"%(lastname.count("박"),lastname.count("이")))

print("\n===2번 문제===")
print("박주형 : %d"%name.count("박주형"))

print("\n===3번 문제===")
sole_name2 = []
for i in name:
    if i not in sole_name2:
        sole_name2.append(i)
# print(sole_name2)
sole_name = list(set(name))
print(sole_name)

print("\n===4번 문제===")
sole_name.sort()
print(sole_name)
