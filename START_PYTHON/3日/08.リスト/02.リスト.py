# 리스트는 담아두는 자료형
# 인덱싱이나 슬라이싱으로 빼서 사용
a = [1, 2 ,3]
print(a)
print(a[0]) # 인덱싱
print(a[0] + a[2])

student = ["kim", "lee","park"]
print(student)
print(student[2])
print(student[2][1])

a = [1,2,3,["a","b","abc"]]
# print(a[5]) 인덱스 범위를 벗어남
print(a[3])
print(a[3][2])
print(a[3][2][2])
