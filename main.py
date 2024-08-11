from turtle import Screen
from paddles import Paddle, PLAYER_1_POSITION, PLAYER_2_POSITION
import time
from ball import Ball
from score_board import Score
from table import Table

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

paddle_1 = Paddle(PLAYER_1_POSITION, "maroon2")
paddle_2 = Paddle(PLAYER_2_POSITION, "blue")
ball = Ball()
score = Score()
table = Table()

screen.listen()
screen.onkey(paddle_1.move_up, "w")
screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_1.move_down, "s")
screen.onkey(paddle_2.move_down, "Down")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_2) < 60 and ball.xcor() > 320
            or ball.distance(paddle_1) < 60 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect when paddle misses + score
    if ball.xcor() > 380:
        score.scoring_1()
        if score.player_1_score == 10:
            score.game_over(score.player_1)
            game_on = False
        ball.reset_ball()

    elif ball.xcor() < -350:
        score.scoring_2()
        if score.player_2_score == 10:
            score.game_over(score.player_2)
            game_on = False
        ball.reset_ball()

screen.exitonclick()
