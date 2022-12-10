from time import sleep
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()
score = Score()
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    sleep(0.05)
    screen.update()
    ball.move()

    # bonces the ball from top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounceX()
        ball.speed()

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounceX()
        ball.speed()

    if ball.xcor() > 380:
        ball.resetPosition()
        score.increseScore1()

    if ball.xcor() < -380:
        ball.resetPosition()
        score.increseScore2()
screen.exitonclick()
