from turtle import Turtle,Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.updateScore()
        # self.clear()

    def updateScore(self):
        self.color("white")
        self.penup()
        self.goto(-50,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", "center", font=('Atari', 15, 'normal'))
    
    def GameOver(self):
        self.goto(-30,0)
        self.write("GAME OVER.", "left", font=('Atari', 17, 'normal'))

    def increseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()