a = [3,5,2,6,1,4]
# len() : 문자열의 길이, 리스트의 요소 개수
print(len(a))
avg = sum(a)/6
print("7을 추가하기 전의 평균 : ",avg)
a.append(7)
avg = sum(a)/ len(a)
print("7을 추가한 후의 평균 : ",avg)
