from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_X = self.xcor() + self.move_x
        new_Y = self.ycor() + self.move_y
        self.goto(new_X,new_Y)

    def bounce(self):
        self.move_y *= -1

    def bounceX(self):
        self.move_x *= -1

    def resetPosition(self):
        self.goto(0,0)
        self.bounceX()

    def speed(self):
        self.move_x += 1
        self.move_y += 1   