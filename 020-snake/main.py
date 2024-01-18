import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

# Starting with snake of length 3
for _ in range(0, 3):
    snake.extend()

continue_game = True
while continue_game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.get_head().distance(food) < 10:
        scoreboard.increment()
        snake.extend()
        food.refresh_position()

    # Detect collision with wall
    # Note: top wall taken to be bottom of the scoreboard
    if snake.get_head().xcor() > 280 or \
            snake.get_head().xcor() < -290 or \
            snake.get_head().ycor() > 270 or \
            snake.get_head().ycor() < -280:
        scoreboard.game_over()
        continue_game = False

    # Detect collision of head with any segment of the tail
    if snake.collision_with_tail():
        scoreboard.game_over()
        continue_game = False

screen.exitonclick()
