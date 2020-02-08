# 조건식을 통해서 내가 원하는 횟수만큼 반복하도록 함.
num = 0 # 초기값

while num <= 3: # 조건식
    print("num = %d"%num)
    num+=1 # 복합대입연산자, 증감식

print("""어제 드라마 봤어?
꼭 봐라! 두 번 봐라!""")
count = 2
while count: # 정수는 0이 되면 거짓말
    print("재방송을 시작합니다.")
    count-=1
print("두 번 다 봤어")

print("열 번 찍어 안 넘어가는 나무 없다.")
hit = 0
while hit <10: # hit 가 10보다 작을때만 반복
    hit += 1
    print("나무를 %d번 찍었습니다."%hit)
print("나무가 넘어갔습니다.")
