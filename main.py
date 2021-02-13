from turtle import Screen
import time
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from bricks import Bricks

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout Baby")
screen.setup(width=600, height=800)
screen.tracer(0)


paddle = Paddle((0, -300))
bricks = Bricks()
scoreboard = Scoreboard()
bricks.make_bricks()


ball = Ball()


screen.listen()
screen.onkey(key="Right", fun=paddle.go_right)
screen.onkey(key="Left", fun=paddle.go_left)


playing = True
lives = 3
while playing:
    screen.update()
    ball.move()

    for brick in bricks.brick_list:
        if ball.distance(brick) < 30:
            bricks.brick_list.remove(brick)
            brick.hideturtle()
            ball.bounce_y()
            scoreboard.point(brick)

    if paddle.distance(ball) < 50 and ball.ycor() < -270:
        ball.bounce_y()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.ycor() < -380:
        ball.reset()
        lives -= 1
        if lives == 0:
            playing = False

    if len(bricks.brick_list) == 0:
        playing = False

screen.exitonclick()

