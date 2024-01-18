from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        self.update_score()

    def increment(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        text = f"Score : {self.score}"
        self.write(text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("*** GAME OVER ***", align=ALIGNMENT, font=FONT)

