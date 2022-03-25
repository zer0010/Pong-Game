from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Welcome to Pong game')
scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.listen()
screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")
screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    time.time()
    screen.update()
    ball.move_random()

    # detects collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detects collision with right pad

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # detects ball with left pad

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect when r_paddle misses

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.refresh_position()

    # detects when l_paddle misses

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.refresh_position()

screen.exitonclick()
