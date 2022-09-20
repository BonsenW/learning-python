from turtle import Turtle

MOVE_DISTANCE = 20
EAST, NORTH, WEST, SOUTH = (0, 90, 180, 270)

class Snake:
    snake_body: list[Turtle] = []

    def __init__(self, length) -> None:
        for i in range(length):
            self.add_bodypart((i * -20, 0))

        self.head = self.snake_body[0]
    
    def extend_body(self):
        self.add_bodypart(self.snake_body[-1].pos())

    def add_bodypart(self, position):
        body_part = Turtle("circle")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.snake_body.append(body_part)
        
    def move_forward(self, steps):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i-1].pos())
        self.head.forward(steps)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
    
    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

