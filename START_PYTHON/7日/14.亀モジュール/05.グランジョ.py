import turtle as t

t.shape("turtle")
t.color("red")
t.pensize(3)
a = 500
b = 144
c = 50
r = 90
#up, down : 종이에 잉크가 묻지않도록 펜을 들고 위, 아래로 이동
t.up() #여기서 꼬랑지에서 펜을 잠시 떼놔요
t.lt(r)
t.fd(c)
t.lt(r)
t.fd(a/2)
t.rt(r*2)
t.down() #여기부터 다시 그리기 시작
for i in range(4):
    t.fd(a)
    t.rt(b)
t.fd(a)
t.lt(126)
t.up()
t.rt(r)
t.fd(20)
t.lt(r)
t.fd(80)
t.down()
t.circle(a/2 + 20)
t.rt(r)
t.up()
t.fd(c)
t.lt(r)
t.down()
t.circle(a/2+c+20)
input()
