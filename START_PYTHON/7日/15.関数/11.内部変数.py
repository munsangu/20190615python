a = 1 # 나
# 함수는 지역이다.
# 외부지역(부산)
# test(서울)
def test(a): #a 나인데 서울 사는 나(동명이인)
    a += 1
    print("함수 내 a : %d"%a)
print("함수 호출 전 a: %d"%a)
test(a) # 나가 간 것이 아니라 나가 들고 있는 값만 보내줬음
print("함수 호출 후 a: %d"%a)

print("\n===== global 명령어 =====")
# c언어 넘어가면 전역변수
# 최대한 쓰지말라고 나옴
# 언어 만드신분들은 천재 -> 함수가 독립적으로 동작해야 에러없이 프로그램이 작동
a = 1
def test():
    global a # 밖의 a와 test의 a가 연결
    a += 1
test()
print("함수 호출 후 a : %d"%a)
