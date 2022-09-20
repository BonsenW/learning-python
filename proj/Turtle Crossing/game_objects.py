from distutils.spawn import spawn
from turtle import Turtle
import random

NORTH, WEST = 90, 180
TURTLE_SPEED = 20
BASE_CARSPEED = 10
CARSPEED_MULTIPLER = 1.1

class Car(Turtle):
    def __init__(self, position: tuple) -> None:
        super().__init__()
        
        # initialises visual properties
        self.shape('square')
        self.color(self.rand_colour())
        self.shapesize(stretch_wid=0.75, stretch_len=1.75)
    
        # physical position
        self.penup()
        self.setheading(WEST)
        self.set_newpos(position)
        self.move_speed = BASE_CARSPEED

    def rand_colour(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)
    
    def move_forward(self):
        self.forward(self.move_speed) 
    
    def set_newpos(self, pos):
        self.goto(pos)
    
    def increase_speed(self):
        self.move_speed *= CARSPEED_MULTIPLER



class BabyTurtle(Turtle):

    def __init__(self, position: tuple) -> None:
        super().__init__()

        self.shape('turtle')
        self.color('black')
        self.penup()

        self.setheading(NORTH)
        self.position = position
        self.reset_position()
    
    def move_forward(self):
        self.forward(TURTLE_SPEED)
    
    def reset_position(self):
        self.goto(self.position)
