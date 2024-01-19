from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "bold")
WINNING_SCORE = 5

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 250)
        self.update_score()

    def increment_left(self):
        self.l_score += 1
        self.update_score()

    def increment_right(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        text = f"{self.l_score} : {self.r_score}"
        self.write(text, align=ALIGNMENT, font=FONT)

    def is_game_over(self) -> bool:
        if self.l_score >= WINNING_SCORE or self.r_score >= WINNING_SCORE:
            self.goto(0, 0)
            self.write("*** GAME OVER ***", align=ALIGNMENT, font=FONT)
            return True
        else:
            return False

