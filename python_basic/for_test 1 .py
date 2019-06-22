'''
test_list = ['one','two','three']
test_list = 'asdaaseddef'
for i in test_list:
    print(i)
'''

'''
a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
'''
'''
sum = 0
for i in range(1,11):
    if i % 2 ==0:
        sum = sum + i
print(sum)
'''
'''
a = input("주민번호 입력: ")
if a[7]== '1' or a[7]== '3':
    print("남자")
elif a[7]== '2' or a[7]== '4':
    print("여자")
'''

'''
for i in range(2,10):
    print("\n--[%d단]--"%i)
    for j in range(1,10):
        print("%d x %d = %d"%(i,j,i*j))
'''

'''
for i in range(1,10):
 
    for j in range(2,10):
        # print("%d x %d = %2d" %(y,x,x*y), end = ' ')
        print("{} x {} = {:2}".format(j,i,i*j),end =' ')
    print()
'''
'''
coffee = {'아메리카노':2500, '카페라떼':3000, '카푸치노':3500}

for i in coffee.keys():
    print(i, end=' ')
print()

a = input("선택: ")
for i,j in coffee.items(): # 튜플로 리턴(키, 값)
    if i == a:
        print(j)
'''
'''
import random

count = 0
for i in range(0,5):
    a = random.randint(1,50)
    b = random.randint(1,50)
    print("%d + %d = "%(a,b))
    c=int(input())
    if a+b == c:
        print("정답!")
        count+=1
    else:
        print("오답!")
print("%d개 맞음"%count)
'''
'''
import random

count = 0
oper = ['+','-','*','/']
for i in range(0,5):
    a = random.randint(1,50)
    b = random.randint(1,50)
    op = random.choice(oper)
    quiz=str(a)+op+str(b)
    print(quiz,'=')
    print(eval(quiz))
    c=int(input("정답 ="))

    if int(eva;(quiz)) == c:
        print("정답!")
        count+=1
    else:
        print("오답!")

print("%d개 맞음"%count)
'''
'''
import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()
input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()
et = end - start
print("실제 시간 :",et,"초")
print("차이 :",abs(et-20),"초")
'''
import random, time

com=random.randint(1,100)
count=0
print('답 :',com)
input("시작!")
start = time.time()
while True:
    input_no = int(input('1~100사이 숫자를 입력하세요 \n'))
    if com == input_no:
        count+=1
        print('정답입니다. {}번만에 맞추셨습니다.'.format(count))
        break
    elif com>input_no:
        count+=1
        print('더 큰수를 입력하세요.')
    else:
        count+=1
        print("더 작은수를 입력하세요.")
end = time.time()
t = end - start
print('걸린 시간은 {:0f}초 입니다.'.format(t))


