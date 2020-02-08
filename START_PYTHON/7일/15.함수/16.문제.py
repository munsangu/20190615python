def avg_scores(**kwargs):
    print(kwargs)
    return sum(kwargs.values()) / len(kwargs)
print("평균 : %.2f"%avg_scores(국어 = 90,영어 = 88, 수학 = 80, 과학 = 70))
