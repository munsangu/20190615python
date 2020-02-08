# 48을 2로 나눴을 때 나머지(0)에 x 1
# 24를 2로 나눴을 때 나머지(0)에 x 10
# 12를 2로 나눴을 때 나머지(0)에 x 100
# 6을 2로 나눴을 때 나머지(0)에 x 1000
# 3을 2로 나눴을 때 나머지(1)에 x 10000
# 1을 2로 나눴을 때 나머지(1)에 x 100000
# 이 값을 모두 더하면 110000이 나오게 된다.
decimal = int(input("10진 정수 입력 : "))
binary = 0
digit = 1 #자릿수 변수
while decimal > 0:
    binary += decimal % 2 * digit
    digit *= 10
    decimal //= 2
print(binary)
