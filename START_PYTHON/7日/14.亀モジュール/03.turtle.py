import turtle as t

# t.shape("turtle")
# t.bgcolor("black") # 배경색
# t.pensize(10) # 거북이 꼬리에 펜의 크기를 결정
#
# t.begin_fill() # 여기부터 색칠
# t.color("white") # 거북이 색깔
# for i in range(3):
#     t.forward(100)
#     t.left(120)
# t.end_fill() # 여기까지 색칠
# input()

# t.shape("classic")
# size = int(input("도형의 크기<50 ~ 100> : "))
# angle = int(input("도형 각의 갯수<3 ~ 8> : "))
# t.pensize(int(input("펜 굵기<1 ~ 10> : ")))
#
# for i in range(angle):
#     t.forward(size)
#     t.left(360/angle)
# input()

# t.shape("triangle")
# t.bgcolor("black")
# t.color("white")
# t.speed(0) # 0이 제일 빠름 -> 10으로 갈수록 느려짐
#
# for i in range(200):
#     t.forward(i)
#     t.lt(55) # left ==> lt  / # forward ==> fd / # right ==> rt
# input()

import random as r
t.shape("turtle")
t.color("blue")
t.speed(0)
for i in range(500):
    t.lt(r.randint(1,360))
    t.fd(r.randint(1,20))
input()
