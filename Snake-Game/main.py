from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score


# setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# importing classes
snake = Snake()
food = Food()
score = Score()
# Keys to press
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # collides with food
    if snake.head.distance(food) < 15:
        print("Collided")
        score.increseScore()
        snake.Extend()
        food.refresh()

    # collides with walls
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.GameOver()
        game_is_on = False

        # collides with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.GameOver()



screen.exitonclick()

