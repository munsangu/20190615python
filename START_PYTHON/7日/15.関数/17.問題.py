def My_avg(*args):
    return sum(args)/len(args)

def My_max(*args):
    max = 0
    for i in args:
        if max <= i:
            max = i
    return max

print("평균: %.2f"%My_avg(97,44,31))
print("쵀대값: %.2f"%My_max(97,44,31))
