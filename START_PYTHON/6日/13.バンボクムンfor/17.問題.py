a = []
num = 1
for i in range(8):
    line = []
    for j in range(8):
        line.append(num)
        num += 1
    a.append(line)
    print(line)
print(a)
