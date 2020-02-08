# range : 범위를 지정 -> 슬라이싱과 유사
print(range(5))
print(list(range(5))) # 0 ~ 4 범위를 지정
print(tuple(range(5))) # 0 ~ 4 범위를 지정
print(list(range(1,10,2)))
# print(list(range('a','z'))) # 정수 형태만 가능

for i in range(5): # 0 ~ 4 -> 5번 반복
    print("i = %d"%i)
for i in range(3, 10): # 3 ~ 9
    print("i = %d"%i)


print("\n=== for + range 활용 ===")
sum = 0
for i in range(1,11): # 1 ~ 10
    sum += i
print("1부터 10까지의 합계 : %d"%sum)

print("\n=== 1 ~ 10까지의 홀수의 합계 ===")
sum = 0
for i in range(1,11,2):
    sum += i
print("1부터 10까지 홀수의 합계 : %d"%sum)

print("\n=== 카운드 다운 ===")
for i in range(10,0,-1):
    print(i)
