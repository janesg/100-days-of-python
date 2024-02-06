from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.move_to_starting_position()

    def move(self):
        pos = self.position()
        if pos[1] < FINISH_LINE_Y:
            self.goto(pos[0], pos[1] + MOVE_DISTANCE)

    def move_to_starting_position(self):
        self.goto(STARTING_POSITION)

    def has_crossed_road(self) -> bool:
        return self.ycor() >= FINISH_LINE_Y
