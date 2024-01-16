from random import randint
from turtle import Turtle, Screen
import colorgram


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = r, g, b
    return color


# Extract colour pallet from Hirst art image
# hirst_colors = colorgram.extract("th-1920986090", 20)
hirst_colors = colorgram.extract("th-3637935002", 20)

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
        # turtle.dot(15, random_color())
        turtle.dot(15, hirst_colors[randint(0, len(hirst_colors) - 1)].rgb)

screen.exitonclick()
