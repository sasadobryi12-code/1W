import turtle
import turtle as t
import random
t = turtle.Turtle()

# Упражнение №3: квадрат

screen = turtle.Screen()

t.shape('turtle')
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

screen.exitonclick()


# Упражнение №4: окружность

screen = turtle.Screen()

t.shape('turtle')
t.circle(100)

screen.exitonclick()

# Упражнение №5: больше квадратов


screen = turtle.Screen()

turtle.bgcolor('black')
t.color('green')
t.pensize(10)

v = 100

for i in range(88):
    for j in range(4):
        t.right(90)
        t.forward(v)
    t.penup()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.pendown()
    v+=40

screen.exitonclick()

# Упражнение №6: паук

screen = turtle.Screen()

turtle.bgcolor('black')
t.color('green')
v = 0
n=9

t.shape('turtle')

if n>=0 & v <=360:
        a = 360/n
        while v!=n:
                t.right(a)
                t.forward(50)
                t.stamp()  
                t.back(50) 
                v+=1

screen.exitonclick()


# Упражнение №7: спираль

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.color('green')

v = 1 

while v < 300:
    t.forward(v)
    t.right(20)
    v += 1

screen.exitonclick()


# Упражнение №8: квадратная «спираль»

screen = turtle.Screen()

turtle.bgcolor('black')
t.color('green')

v = 0

while v < 20:
        t.forward(v)
        t.right(90)
        v+=1

screen.exitonclick()

# Упражнение №9: правильные многоугольники

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.color('green')
t.shape('turtle')


n = 6
v = 40

def draw_polygon(n, v):
    angle = 360 / n
    for i in range(n):
        t.forward(v)
        t.left(angle)

for i in range(10):
    draw_polygon(n, v)
    v += 15
    t.penup()
    t.right(90)
    t.forward(12)
    t.right(90)
    t.forward(8)
    t.pendown()
    t.setheading(0)
screen.exitonclick()

# Упражнение №10: «цветок»

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.color('green')
t.shape('turtle')

c = 360
n = 5

if n>=0 & n<=360:
    angle=c/n
    k=0
    while k!=n:
        t.circle(40)
        t.right(angle)
        k+=1
    screen.exitonclick()

# Упражнение №11: «бабочка»

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.color('green')
t.shape('turtle')
t.left(90)

r=50
n=2
k=0
while k!=n:
    t.right(0)
    t.circle(r)
    t.circle(-r)
    r+=7
    k+=1

screen.exitonclick()

# Упражнение №12: пружина

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.color('green')
t.shape('turtle')

t.penup()
t.left(180)
t.forward(200)
t.pendown()
for i in range(4):
    t.setheading(90)
    t.circle(-50, 180)
    t.circle(-10, 180)
t.circle(-50, 180)
screen.exitonclick()
