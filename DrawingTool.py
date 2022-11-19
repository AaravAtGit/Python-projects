# use Space to move forward
# use a and d to move left and right

from turtle import Turtle,Screen

mr_turtle = Turtle()
screen = Screen()

def move():
    mr_turtle.forward(50)

def turnleft():
    mr_turtle.left(10)

def turnright():
    mr_turtle.right(10)

def back():
    mr_turtle.backward(50)

def clears():
    mr_turtle.clear()
    mr_turtle.penup()
    mr_turtle.setpos(0,0)
    mr_turtle.pendown()

screen.listen()
screen.onkeypress(move,"space")
screen.onkeypress(turnleft,"a")
screen.onkeypress(turnright,"d")
screen.onkeypress(back,"s")
screen.onkey(clears,"c")

screen.exitonclick()

