import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(800, 800)
screen.title("Спираль")

t = turtle.Turtle()
t.color("black")
t.pensize(1)

angle = 10
step = 0.3
length = 2
loops = 600

for i in range(loops):
    t.forward(length)
    t.right(angle)
    length += step


turtle.done()
