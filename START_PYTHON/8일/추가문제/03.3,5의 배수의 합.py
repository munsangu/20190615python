total = 0
for i in range(1,1001):
    if i%3 == 0 or i%5 == 0:
        total += i
print(total)

print(sum(list([x for x in range(1001) if x%3==0 or x%5==0])))
