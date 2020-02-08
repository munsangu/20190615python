num1 = int(input("정수1: "))
num2 = int(input("정수2: "))
i = 1

# 최소공배수 구하는 코드
while True: # 무한 반복문  : 조건식이 거짓이 안되는 무한반복문
    if i % num1 == 0 and i % num2 == 0:
        break #반복문종료
    i+=1
print("최소공배수 : %d"%i)

while 1: # 0이 아니면 True : 무한 반복문종료
    string = input("알파벳을 입력(q를 눌면 종료) : ")
    if string == 'q':
        break
    else:
        string = string.capitalize() # 첫 글자를 대문자로 변환
        print(string)
