from turtle import Turtle

ALLIGNMENT = "CENTER"
FONT = ("Ariel", 24, "normal")

class LevelManager(Turtle):
    def __init__(self, text_position):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()

        self.level = 1
        self.goto(text_position) # 0, 250
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Level = {self.level}", align=ALLIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!", align=ALLIGNMENT, font=FONT)

