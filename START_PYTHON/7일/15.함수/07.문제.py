def fiveover(a): # a = numlist
    result = []
    for i in a:
        if i > 5:
            result.append(i)
    return result

numlist = []
for i in range(5):
    numlist.append(int(input("%d번째 정수 입력: "%(i+1))))
result = fiveover(numlist) # numlist를 fiveover에게 전달
print(result)
