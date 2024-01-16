from turtle import Turtle, Screen


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_right():
    # turtle.right(10)
    turtle.setheading(turtle.heading() - 10)

def move_left():
    # turtle.left(10)
    turtle.setheading(turtle.heading() + 10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle = Turtle()
turtle.shape("turtle")

screen = Screen()
screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "space", fun = clear)


screen.exitonclick()
