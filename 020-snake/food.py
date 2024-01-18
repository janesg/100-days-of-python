import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        # Reduce default 20 x 20 to 10 x 10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        # Ensure food appears in position immediately
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        # Max y is smaller to allow for score text
        self.goto(random.randint(-285, 285), random.randint(-285, 265))
