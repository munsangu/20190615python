a = [10,22,33,44,50]
a[1:4] = [20,30,40]
print(a)
del a[2]
print(a)

b = [21, 9, 12, 17, 9, 3, 27, 32, 1]
b[2:4] = [22,7]
b[7:8] = [19]
print(b)
# 변수명[a:b:c] -> a부터 b-1까지 c만큼 건너뛰면서 슬라이싱
# sum() : 안에 들어간 값을 전부 더해주는함수
# sum(b[::2]) -> 홀수번째 갯수의 합
# sum(b[1::2]) -> 짝수번째 갯수의 합
odd = sum(b[::2])
even = sum(b[1::2])
print("홀수번째 내용의 합 : ",odd, "\n짝수번째 내용의 합 : " ,even)

c = [5,9,1,2,10,15]
print("최대값 : ", max(c), "\n최소값 : ", min(c))
