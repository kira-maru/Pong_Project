from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_1_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.player_2_score, align="center", font=("Courier", 70, "normal"))

    def scoring_1(self):
        self.player_1_score += 1
        self.update_score()

    def scoring_2(self):
        self.player_2_score += 1
        self.update_score()