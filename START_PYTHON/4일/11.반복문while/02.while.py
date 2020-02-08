import os # system 함수를 들고있는 개체
num = 0
while True: # 조건식이 거짓말이 안되는 반복문 => 무한반복문
    print("""
    =====메뉴=====
    1. 정수 입력
    2. 입력된 정수 출력
    3. 종료
    """)
    select = int(input("메뉴 선택 : "))
    if select == 1:
        num = int(input("정수 입력: "))
    elif select ==2:
        print("입력된 정수 : %d"%num)
    else:
        exit(0) # 프로그램 종료
    os.system("pause") # 코드 일시 정지
    os.system("cls")   # 콘솔창을 깨끗하게 지워줌
