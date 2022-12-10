from turtle import Turtle,Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.updateScore()

    def updateScore(self):
        self.color("white")
        self.penup()
        self.goto(-50,270)
        self.hideturtle()
        self.write(f"Score {self.score1}:{self.score2}", "center", font=('Atari', 15, 'normal'))
    

    def increseScore1(self):
        self.score1 += 1
        self.clear()
        self.updateScore()
    
    def increseScore2(self):
        self.score2 += 1
        self.clear()
        self.updateScore()

