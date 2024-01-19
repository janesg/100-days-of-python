from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position: (float,float)):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("normal")
        self.shape("square")
        self.shapesize(stretch_wid=4.0, stretch_len=1.0)
        self.goto(position)

    def move_up(self):
        pos = self.position()
        if pos[1] < 260:
            self.goto(pos[0], pos[1] + 20)

    def move_down(self):
        pos = self.position()
        if pos[1] > -255:
            self.goto(pos[0], pos[1] - 20)

