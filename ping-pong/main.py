from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

ball = Ball()
score = Score()
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and (r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50)
            or ball.xcor() < -320 and (l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50)):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
