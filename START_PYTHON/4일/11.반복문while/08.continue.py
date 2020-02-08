# while, break, continue : 다른 언어에서 그대로 나옴
num = int(input("정수 입력: "))
print("=== 3의 배수 출력 ===")
#9 => 3, 6, 9
i = 0
while i <num:
    i+=1
    if i % 3 !=0:
        continue # 반본문의 조건식(처음)으로 이동
    print(i,end=" ")

while True:
    value = input("정수 입력[q to quit] : ") #문자열로 입력
    if value == 'q':
        break #반복문 종료
    num = int(value) #정수로 바꿔서 저장
    if num % 2 != 0:
        continue #다시 조건식으로 돌아감(아래의 문장을 실행하지 않음)
    print("%d is evennumber"%num)
