from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial', 24, "bold")
class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 250)

        self.updateScoreboard()

        self.hideturtle()
    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\nScore:{self.score}",align=ALIGNMENT,font=FONT)

    def updateScoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)


    def increaseScore(self):
        self.score+=1
        self.clear()
        self.updateScoreboard()


