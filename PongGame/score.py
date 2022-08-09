from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")
DASH = 15


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.dashed()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.dashed()
        self.goto(-100, 200)
        self.write(arg=f"{self.score_l}", align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.score_r}", align=ALIGN, font=FONT)

    def increase_score_left(self):
        self.score_l += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_r += 1
        self.update_scoreboard()

    def dashed(self):
        self.shapesize(stretch_wid=3, stretch_len=3, outline=3)
        self.goto(0, -290)
        self.setheading(90)
        for _ in range(30):
            self.pendown()
            self.forward(DASH)
            self.penup()
            self.forward(DASH)
            self.pendown()
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)