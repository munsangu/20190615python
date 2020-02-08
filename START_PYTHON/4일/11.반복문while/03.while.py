# 내가 원하는 만큼 입력받고 그 숫자의 평균을 구하는 프로그램
num = 1
count = 0
sum = 0
while num !=0: #num이 0이 아니면 반복
    num = int(input("정수 입력: "))
    count += 1 # 몇 번 입력받았는지 count
    sum += num
count -= 1 # 0을 입력한 count 하나 제외
avg = sum / count
print("평균 : %.2f"%avg)
