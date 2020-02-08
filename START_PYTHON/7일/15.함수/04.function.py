import turtle as t
# setheading() : 거북이의 방향을 원하는 각도로 바꿔줌
def move_right():
    t.setheading(0)
    t.fd(10)
def move_up():
    t.setheading(90)
    t.fd(10)
def move_left():
    t.setheading(180)
    t.fd(10)
def move_down():
    t.setheading(270)
    t.fd(10)
def circle():
    t.circle(50)
def triangle():
    for i in range(3):
        t.lt(120)
        t.fd(100)
def square():
    for i in range(4):
        t.lt(90)
        t.fd(100)
def star():
    for i in range(5):
        t.fd(100)
        t.rt(144)

t.shape("turtle")
t.speed(5)
t.onkeypress(move_up,"Up")
t.onkeypress(move_down,"Down")
t.onkeypress(move_right,"Right")
t.onkeypress(move_left,"Left")
t.onkeypress(circle,"c")
t.onkeypress(triangle,"t")
t.onkeypress(square,"s")
t.onkeypress(star,"*")

t.listen()
t.mainloop()
input()
