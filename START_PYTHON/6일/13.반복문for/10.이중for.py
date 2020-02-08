for i in range(3): # 바깥의 for가 한 번 반복할 때 안의  for는 처음부터 끝까지 반복
    print("====={0}학년=====".format(i + 1))
    for j in range(5):
        print("-----{0}학년--{1}반---".format(i+1,j+1))

# 보통 횟수가 정해져 있으면 for
# 횟수를 잘 모를때는 while
print("\n=====이중 for로 구구단 =====")
for i in range(2,10):
    for j in range(1,10):
        print("%d x %d = %d"%(i,j,i*j))
    print() # 엔터키

print("\n=====이중 whlie로 구구단 =====")
a, b = 2 , 1
while a < 10:
    while b < 10:
        print("%d x %d = %d"%(a,b,a*b))
        b += 1
    a += 1
    b = 1
    print()
