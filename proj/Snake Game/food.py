from mimetypes import init
from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.rand_colour())
        self.speed(0)
        self.refresh()
        
    def rand_colour(self):
        r = random.randrange(50, 255)
        g = random.randrange(50, 255)
        b = random.randrange(50, 255)
        return (r,g,b)
    
    def refresh(self):
        new_pos = (random.randint(-200, 200), random.randint(-200, 200))
        self.goto(new_pos)

if __name__ == "__main__":
    screen = Screen()
    screen.colormode(255)

    x = Food()

    screen.exitonclick()