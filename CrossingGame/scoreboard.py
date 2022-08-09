from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-295, 265)
        self.write(arg=f"Level: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)
