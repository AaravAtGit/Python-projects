from turtle import Turtle

FONT = ("BOLD", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.scores = Turtle()
        self.scores.penup()
        self.scores.color("black")
        self.scores.goto(-290,260)
        self.scores.hideturtle()
        self.level = 1
        self.scores.write(f"Level:{self.level} ",align="left",font=FONT)


    def gameOver(self):
        over = Turtle()
        over.penup()
        over.color("black")
        over.hideturtle()
        over.write("GAME OVER.",align="center", font=FONT)


    def score_tracker(self):
        self.level += 1
        self.scores.clear()
        self.scores.write(f"Level:{self.level} ",align="left",font=FONT)

