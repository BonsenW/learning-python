from turtle import Turtle

ALLIGNMENT = "CENTER"
FONT = ("Ariel", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", 'r') as hs:
            for num in hs.readlines():
                self.high_score = int(num.strip())
        
        self.current_score = 0

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}", align=ALLIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()
    
    def check_highscore(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("highscore.txt", 'w') as hs:
                hs.write(str(self.high_score))

    def game_over(self):
        self.check_highscore()
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALLIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(f"High Score: {self.high_score}", align=ALLIGNMENT, font=FONT)