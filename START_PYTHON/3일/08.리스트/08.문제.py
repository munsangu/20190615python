moon = [input("이름 : "),int(input("나이: ")), float(input("왼쪽 시력 : ")), float(input("오른쪽 시력 : "))]
print(moon)
lee = [input("이름 : "),int(input("나이: ")), float(input("왼쪽 시력 : ")), float(input("오른쪽 시력 : "))]
print(lee)

num1 = int(moon[1] + lee[1]) / 2
print("조원의 평균 나이 : ", num1)
#print("나이 : %2.f"%((moon[1]+lee[1])/2))
num2 = float(moon[3]+lee[3]) / 2
print("조원의 평균 오른쪽 시력 :", num2)
#print("시력 : %.2f"%((moon[3]+lee[3])/2))
