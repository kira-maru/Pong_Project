PLAYER_1_POSITION = [(-380, 0), (-380, 20), (-380, 40), (-380, 60)]
PLAYER_2_POSITION = [(380, 0), (380, 20), (380, 40), (380, 60)]
MOVE_CONSTANT = 10
from turtle import Turtle

class Paddle:

    def __init__(self):
        self.player_1_paddle = []
        self.player_2_paddle = []
        self.create_paddle()
        self.head_1 = self.player_1_paddle[-1]
        self.tail_1 = self.player_1_paddle[0]
        self.head_2 = self.player_2_paddle[-1]
        self.tail_2 = self.player_2_paddle[0]

    def create_paddle(self):
        for position in PLAYER_1_POSITION:
            self.add_segment_1(position)
        for position in PLAYER_2_POSITION:
            self.add_segment_2(position)

    def add_segment_1(self, position):
        new_segment = Turtle("square")
        new_segment.color("maroon2")
        new_segment.penup()
        new_segment.goto(position)
        self.player_1_paddle.append(new_segment)

    def add_segment_2(self, position):
        new_segment = Turtle("square")
        new_segment.color("blue")
        new_segment.penup()
        new_segment.goto(position)
        self.player_2_paddle.append(new_segment)

    def move_up_1(self):
        tail_y = self.tail_1.ycor()
        self.tail_1.goto(self.tail_1.xcor(), tail_y + MOVE_CONSTANT)

        for i in range(len(self.player_1_paddle) - 1, 0, -1):
            new_x = self.player_1_paddle[i - 1].xcor()
            new_y = self.player_1_paddle[i - 1].ycor()
            self.player_1_paddle[i].goto(new_x, new_y)

    def move_down_1(self):
        head_y = self.head_1.ycor()
        self.head_1.goto(self.head_1.xcor(), head_y - MOVE_CONSTANT)

        for i in range(1, len(self.player_1_paddle)):
            new_x = self.player_1_paddle[i].xcor()
            new_y = self.player_1_paddle[i].ycor()
            self.player_1_paddle[i - 1].goto(new_x, new_y)

    def move_up_2(self):
        tail_y = self.tail_2.ycor()
        self.tail_2.goto(self.tail_2.xcor(), tail_y + MOVE_CONSTANT)

        for i in range(len(self.player_2_paddle) - 1, 0, -1):
            new_x = self.player_2_paddle[i - 1].xcor()
            new_y = self.player_2_paddle[i - 1].ycor()
            self.player_2_paddle[i].goto(new_x, new_y)

    def move_down_2(self):
        head_y = self.head_2.ycor()
        self.head_2.goto(self.head_2.xcor(), head_y - MOVE_CONSTANT)

        for i in range(1, len(self.player_2_paddle)):
            new_x = self.player_2_paddle[i].xcor()
            new_y = self.player_2_paddle[i].ycor()
            self.player_2_paddle[i - 1].goto(new_x, new_y)

    def up_1(self):
        self.move_up_1()

    def down_1(self):
        self.move_down_1()

    def up_2(self):
        self.move_up_2()

    def down_2(self):
        self.move_down_2()











