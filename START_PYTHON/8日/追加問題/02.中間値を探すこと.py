def median(x):
    x.sort()
    return x[len(x)//2]
answer_list = []
num = int(input("입력할 숫자 갯수 : "))
for i in range(num):
    answer_list.append(int(input("숫자 입력 : ")))
print(median(answer_list))
