# num = int(input("숫자 입력: "))
# a = 0
# for i in range(2, num):
#     if num % i ==0:
#         a = 1
#         break
# if a == 0:
#     print("소수입니다.")
# else:
#     print("소수가 아닙니다.")

num = int(input("숫자 입력: "))
count = 0 # 한 번 나눠질때마다 숫자를 세어줌.
for i in range(1,num+1):
    if num % i == 0: # 나눠지면 i는 num의 약수
        count+=1
if count == 2:
    print("%d는 소수입니다."%num)
else:
    print("%d는 소수가 아닙니다."%num)
