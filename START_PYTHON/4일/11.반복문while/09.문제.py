num = 0
sum = 0
while num <1000:
    num += 1
    if num % 3==0 and num % 5 ==0:
        sum += num
    if num % 3==0:
        continue
    sum += num
print(sum)
