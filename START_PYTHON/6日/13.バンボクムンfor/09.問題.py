#최대공약수 10, 20 => 1 ~ 작은놈까지
#리스트를 만들거나 혹은 변수에 저장하는 방법
MAX_list = [] #공약수를 넣을 리스트
MAX = 0 #공약수를 넣을 변수
num1, num2 =int(input("첫 번째 정수 : ")),int(input("두 번째 정수 : "))

for i in range(1,min(num1,num2) + 1): # 1 ~ 작은 숫자까지
    if num1 % i == 0 and num2 % i == 0: #공약수
        MAX_list.append(i)
        MAX = i
print("최대공약수 : %d"%MAX_list[-1])
print("최대공약수 : %d"%max(MAX_list))
print("최대공약수 : %d"%MAX)
