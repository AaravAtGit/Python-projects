import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player() 
car = CarManager()
score = Scoreboard()
screen.listen()

screen.onkeypress(player.moveup,"w")
screen.onkeypress(player.moveup,"Up")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter % 6 == 0:
        car.create()
    car.move()
    counter += 1

    for cAr in car.cars:
        if cAr.distance(player) < 23:
            game_is_on = False
            score.gameOver()
    
    if player.ycor() > 280:
        player.resetpos()
        car.Speed()
        score.score_tracker()

screen.exitonclick()