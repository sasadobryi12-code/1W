import turtle
import turtle as t
import random
t = turtle.Turtle()

# Задание 1

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


# Задание 2

screen = turtle.Screen()

t.shape('turtle')
t.circle(100)

screen.exitonclick()

# Задание 3


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

# Задание 4


screen = turtle.Screen()

turtle.bgcolor('black')
t.color('green')
v = 0

t.shape('turtle')
t.forward(50)
t.stamp()
for i in range(12):
    t.right(180)
    t.forward(50)
    t.right(v)
    t.forward(50)
    t.stamp()
    v+=45

screen.exitonclick()

# Задание 5

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


# Задание 6

screen = turtle.Screen()

turtle.bgcolor('black')
t.color('green')

v = 0

while v < 20:
        t.forward(v)
        t.right(90)
        v+=1

screen.exitonclick()
