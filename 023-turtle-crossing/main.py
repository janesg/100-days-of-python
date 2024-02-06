import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
# Turn off the tracer - i.e. automatic screen updates
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

continue_game = True
while continue_game:
    # Explicitly get screen to update every 0.1 seconds
    time.sleep(0.1)
    screen.update()

    # Throttle the creation of new cars: 20% chance of adding another car
    if random.randint(1, 5) == 1:
        car_manager.add_another_car()

    car_manager.move_cars()

    # Check for collision between player and car
    if car_manager.has_collided(player):
        scoreboard.game_over()
        continue_game = False

    if player.has_crossed_road():
        scoreboard.level_up()
        player.move_to_starting_position()
        car_manager.level_up()

screen.exitonclick()
