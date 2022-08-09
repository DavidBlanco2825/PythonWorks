# TODO Scoreboard
# The number and the middle das line

# TODO Surfaces
# The paddles an the upper an lower borders of the screen make the
# ball bounce

# TODO the ball
# Make the ball that is continue moving and bounce with the paddles
# and the upper and lower surfaces
# when hits the right or left surfaces a score is made and the ball
# needs to be repositioned

from turtle import Screen
from score import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game.")
screen.tracer(0)

scoreboard = ScoreBoard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()

screen.onkeypress(r_paddle.up, "Up")  # 90
screen.onkeypress(r_paddle.down, "Down")  # 270
screen.onkeypress(l_paddle.up, "w")  # 90
screen.onkeypress(l_paddle.down, "s")  # 270

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 375:
        scoreboard.increase_score_left()
        ball.refresh()

    if ball.xcor() < -375:
        scoreboard.increase_score_right()
        ball.refresh()

screen.exitonclick()
