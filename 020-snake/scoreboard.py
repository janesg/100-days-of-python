from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")
HIGHSCORE_FILE_NAME = "highscore.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        self.high_score = self.read_highscore()
        self.update_score()

    @staticmethod
    def read_highscore() -> int:
        try:
            with open(HIGHSCORE_FILE_NAME) as hs:
                return int(hs.read())
        except FileNotFoundError:
            return 0

    @staticmethod
    def write_highscore(score):
        with open(HIGHSCORE_FILE_NAME, "w") as hs:
            hs.write(f"{score}")

    def increment(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        text = f"Score : {self.score} | High Score : {self.high_score}"
        self.write(text, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore(self.high_score)

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("*** GAME OVER ***", align=ALIGNMENT, font=FONT)

