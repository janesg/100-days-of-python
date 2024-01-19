import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-378, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="a", fun=l_paddle.move_up)
screen.onkeypress(key="z", fun=l_paddle.move_down)
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)

continue_game = True
while continue_game:
    time.sleep(ball.get_move_speed())
    screen.update()

    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 30 and ball.xcor() > 350) or \
            (ball.distance(l_paddle) < 30 and ball.xcor() < -350):
        ball.bounce_x()

    # Detect point scored by left because right missed
    if ball.xcor() > 395:
        scoreboard.increment_left()
        ball.reset_position()

    # Detect point scored by right because left missed
    if ball.xcor() < -395:
        scoreboard.increment_right()
        ball.reset_position()

    if scoreboard.is_game_over():
        continue_game = False

screen.exitonclick()
