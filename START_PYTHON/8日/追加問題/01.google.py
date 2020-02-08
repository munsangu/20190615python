count = 0
for i in range(1, 10001):
    count += str(i).count("8")
print(count)
print(str(list(range(1,10001))).count("8"))
