import turtle
import random


turtle.Screen().bgcolor("black")


t = turtle.Turtle()


def pen_colour(colour):
    t.color(colour)


def fireworks(distance):
    for _ in range(20):
        t.forward(distance)
        t.right(180 - (360 / 20))


def move():
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.pendown()

t.speed(0)

colors = ['red', 'purple', 'green' , 'orange', 'yellow', 'red']


for _ in range (30):
    pen_colour(random.choice(colors))
    fireworks(random.randint(50, 100))
    move()

turtle.done()