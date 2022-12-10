from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []


    def create(self):

        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        Y = random.randint(-230,230)
        new_car.goto(280,Y)
        new_car.setheading(180)
        self.cars.append(new_car)
        self.speed = 5


    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def Speed(self):
        self.speed += 10
