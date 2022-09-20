from turtle import Turtle
import random

MOVE_SPEED = 20
BALL_SPEED = 10
BASE_COLOUR = 'white'

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()

        self.shape('square')
        self.color(BASE_COLOUR)
        self.shapesize(stretch_wid=5,stretch_len=1)

        self.penup()
        self.move_speed = MOVE_SPEED
        self.starting_pos = position
        self.reset_position()
    
    def loop_around_up(self):
        self.goto(self.xcor(), -self.ycor()+MOVE_SPEED)
    
    def loop_around_down(self):
        self.goto(self.xcor(), -self.ycor()-MOVE_SPEED)

    def move_up(self):
        new_pos = self.ycor() + self.move_speed
        self.goto(self.xcor(), new_pos)

    def move_down(self):
        new_pos = self.ycor() - self.move_speed
        self.goto(self.xcor(), new_pos)
            
    def reset_position(self):
        self.goto(self.starting_pos)

class Paddle_AI(Paddle):
    def __init__(self, position, difficulty: str = 'easy') -> None:
        super().__init__(position)
        self.move_speed = MOVE_SPEED/8 if difficulty == 'easy' else MOVE_SPEED/4 if difficulty == 'medium' else MOVE_SPEED
    
    def track_ball(self, ball = Turtle):
        ball_ycor = ball.ycor()
        if self.ycor() > ball_ycor:
            self.move_down()
        elif self.ycor() < ball_ycor:
            self.move_up()

class PaddleBall(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color(BASE_COLOUR)
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.setheading(0)
        self.penup()

        self.direction = 1
        self.ball_speed = BALL_SPEED
        
        rand_angle = random.randint(-67, 67)
        self.setheading(rand_angle)

    def move(self):
        self.velocity = self.ball_speed * self.direction
        self.forward(self.velocity)
        
    def change_angle_dir(self):
        self.setheading(self.heading() * -1)
    
    def change_velocity_dir(self):
        self.direction *= -1
    
    def reset_position(self):
        self.goto(0,0)

        self.ball_speed = BALL_SPEED
        self.change_velocity_dir()
    
        rand_angle = random.randint(-67, 67)
        self.setheading(rand_angle)
    
    def increase_speed(self):
        self.ball_speed *= 1.1