from random import randint
from turtle import Turtle, Screen


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = r, g, b
    return color


screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.hideturtle()
turtle.goto(-270, -240)
turtle.speed(0)

for j in range(-240, 270, 30):
    for i in range(-270, 300, 30):
        turtle.goto(i, j)
        turtle.dot(15, random_color())

screen.exitonclick()
