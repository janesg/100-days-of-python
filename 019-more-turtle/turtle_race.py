from random import randint
from turtle import Turtle, Screen


colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles: list[Turtle] = []

screen = Screen()
screen.setup(width=500, height=400)

colour = screen.textinput("Turtle Race", "Which colour turtle do you think will win the race ?")

if colours.count(colour) == 0:
    print(f"The colour you input, {colour}, is not valid")
    screen.bye()
    exit(0)

for i in range(0, len(colours)):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.goto(-240, -125 + (i * 50))
    turtle.speed(2)
    turtles.append(turtle)

finished = False
winner = None
while not finished:
    # select a random turtle and move it forward
    t = turtles[randint(0, len(turtles) - 1)]
    t.forward(3)
    # check the x co-ordinate for the finish line
    # Note: position is at rear of turtle which has length of 20
    if t.pos()[0] >= 235:
        winner = t.color()[0]
        finished = True

if colour == winner:
    print(f"You win, the {winner} turtle crossed the line first")
else:
    print(f"You lose, the {winner} turtle beat the {colour} turtle to the line")

screen.bye()
exit(0)

