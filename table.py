from turtle import Turtle

class Table(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.pensize(3)
        self.drawing_lines()

    def drawing_lines(self):
        self.setheading(270)
        for _ in range(10):
            self.pendown()
            self.fd(30)
            self.penup()
            self.fd(30)

