from turtle import Turtle

ALLIGNMENT = "CENTER"
FONT = ("Ariel", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

        self.goto(0, 250)
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"{self.p1_score} : {self.p2_score}", align=ALLIGNMENT, font=FONT)

    def add_p1_score(self):
        self.p1_score += 1
        self.clear()
        self.update_scoreboard()
    
    def add_p2_score(self):
        self.p2_score += 1
        self.clear()
        self.update_scoreboard()