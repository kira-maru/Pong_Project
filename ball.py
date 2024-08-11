from turtle import Turtle, Screen
screen = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        color_choice = screen.textinput("Ball color", "Type color of ball: ").lower()
        self.shape("circle")
        self.color(color_choice)
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bounce mechanism
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # reset position after paddle miss
    def reset_ball(self):
        self.home()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10
        self.bounce_x()








