kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
sum = kor + eng + math
avg = sum / 3
print("합계 : %s, 평균 : %.2f"%(sum,avg))
