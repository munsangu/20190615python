import os # 모듈 : system 함수를 사용하기 위한 모듈
while True:
    i = 1 # 곱해줄 수를 항상 1로 초기화
    num = int(input("몇 단?(0을 입력 시 종료) : "))
    if num ==0:
        print("구구단 프로그램을 종료합니다. ")
        break
    while i < 10: # i가 1 ~ 9 까지 반복
        print("%d x %d = %d"%(num,i,num*i))
        i+=1
    os.system("pause") # 코드 일시정지
    os.system("cls") # 콘솔창을 지워줌.
