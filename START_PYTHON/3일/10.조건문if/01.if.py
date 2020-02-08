# time = float(input("현재 시간: "))
# # C언어는 종속문장을 {}로 묶어서 사용
# # 파이썬은 공백으로 구분 => 스페이스바 4번 또는 탭키를 치자고 약속
# if time >= 19.5: # 옆의 조건식을 컴퓨터한테 확인 => 맞으면 if의 종속 문장을 실행
#     print("집에 갑시다~")
#     print("배도 고프니까 저녁도 먹으로 갑시다~")
# else: # if의 조건식이 False면 아래의 종속문장을 실행
#     print("공부 합시다 ^^")
# print("우리 내일도 공부하러 와야되네요^^")

# C언어는 printf("\n"); 출력문 뒤에 \n 키를 붙여줘야 함.
# 파이썬은 print()내부에 end라는 공간에 '\n'키를 숨겨놨음
# age = int(input("당신의 나이를 입력 :"))
# if age>19:
#     print("당신은 성인",end="★")
# else:
#     print("당신은 미성년자",end="★")
# print("입니다.")

money = True #Bool 자료형: 컴퓨터가 대답해주는 형태(True, False)
print("케이크 집에 가서", end="")

if money: #True
    print("먹는다")
    print("냠냠")
else: #False
    print("손가락만 빨고있어")

num = int(input("정수 입력: "))
if num < 0:
    print("%d는 음의 정수"%num, end="")
else:
    print("%d는 양의 정수"%num, end="")
print("입니다.")
