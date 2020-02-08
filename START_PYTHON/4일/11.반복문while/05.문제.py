print("\n=====문제1=====")
num = int(input("숫자를 입력하세요: "))
count = 1
sum = 0

while count <= num:
    sum+= count
    count += 1
print("1부터 %d까지의 누적 합계 : %d"%(num,sum))

print("\n=====문제2=====")
count = 0
while count < 10:
    print("Hello Python")
    count += 1

print("\n=====문제3=====")
sum = 0
num = 1
while num: # 숫자가 0이 됬다 => False
    num = int(input("숫자를 입력하세요(0을 입력시 종료): "))
    sum += num
    print(sum)



print("\n=====문제4=====")
# #1234 => 4321
# #1234 => 4
# #123 => 3
# #12 => 2
# #1 => 1
# #//(몫기호), %(나머지 기호)
num = int(input("정수 입력: "))
reverse = 0
while num !=0:
    reverse = reverse * 10 + num % 10
    num = num //10
print(reverse)
# while num != 0:
#     print(num % 10, end="")
#     num = num // 10

print("\n=====문제5=====")
num = int(input("정수를 입력하세요: "))
count = 1
while count <= num:
    print("%d"%(num*count),end=" ")
    count += 1
