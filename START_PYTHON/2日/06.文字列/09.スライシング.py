a = "You need Python"
# 문자열변수[a:]
# a부터 마지막까지 슬라이싱
print(a[9:])

# 문자열변수[:a-1]
# 처음부터 a-1까지 슬라이싱
print(a[:8])

# 문자열변수[:]
# 처음부터 끝까지 슬라이싱 -> 리스트 배울때 다시 볼 예정
print(a[:])

#문자열변수[start:end-1:step]
#step은 생략하면 1
a = "123456789"
even = a[1::2]
odd  = a[::2]
reverse = a[::-1]
print(even)
print(odd)
print(reverse)
