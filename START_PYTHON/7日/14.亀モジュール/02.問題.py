# import turtle as t
#
# t.shape("turtle")
# t.circle(50)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(120)
# t.forward(60)
# t.right(60)
# t.forward(60)
# t.left(60)
# input()

import turtle as t
import math

t.shape("turtle")
for i in range(4):
    t.forward(100)
    t.right(90)
t.circle(-50)
t.right(90)
t.forward(100)
t.left(135)
t.forward(math.sqrt((100**2)//2))
t.right(90)
t.forward(70)

input()
# math.sqrt() # 제곱근
