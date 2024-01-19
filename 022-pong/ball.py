import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("normal")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        pos = self.position()
        self.goto(pos[0] + self.x_move, pos[1] + self.y_move)

    def bounce_y(self):
        # Add small random angle change off top/bottom walls
        self.y_move += random.randint(0, 3)
        self.y_move *= -1

    def bounce_x(self):
        # Each bounce off a paddle should slightly increase the speed the ball moves at
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        # Serve next ball to winner by reversing x direction
        self.bounce_x()

    def get_move_speed(self):
        return self.move_speed
