a = [[10,20],[30,40],[50,60]]
print(a)

a = [[10,20],
    [30,40],
    [50,60]]
print(a)

print("\n===== 2차원 리스트 접근 방법 =====")
# 이차원 리스트[행][열]
a[0][0] = 1000
a[1][1] = 2000
a[2][1] = 3000
print(a)

for x,y in a:
    print(x,y)

print("\n ===== 2중 for문 리스트 출력 =====")
a = [[10,20,30],
    [40,50],
    [60,70,80,90]]

for i in range(len(a)): #3 : 행
    for j in range(len(a[i])): #3, 2, 4 : 열
        print(a[i][j],end=" ")
    print()

print("\n ===== 2중 for문 리스트 초기화 =====")
a = [] # 바깥 리스트
num = 10
for i in range(8): # 행
    line = [] # 안쪽 리스트
    for j in range(8): # 열
        line.append(num) # extend로 넣었을때는 리스트의 요소로 들어가고 append는 통째로 들어감
        num += 10
    a.append(line)
print(a)

# 파이썬 개발자가 귀차니즘 => 문법을 줄여쓰려고 함.
print("\n ===== 리스트 표현식을 이용한 2중 리스트 =====")
# 중급자용
# 오른쪽 문장이 완벽히 실행됬을때 왼쪽을 실행결과 함.
# [1]
# [1,2]
# [1,2,3]
# [1,2,3,4]
# [1,2,3,4,5]
number_list = [num for num in range(1,6)]
print(number_list)

# 짝수만 저장된 리스트 제작
number_list = [num for num in range(1,11) if num % 2 ==0]
print(number_list)

# 2차원 리스트
a = [[num for j in range(2)] for i in range(3)]
print(a)
