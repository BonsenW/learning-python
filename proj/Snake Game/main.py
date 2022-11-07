from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

# -------------------------------------------------------------------------- #
# ---------------------------------- INIT ---------------------------------- #

screen = Screen()
screen.setup(width=500, height=500)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
        
# -------------------------------------------------------------------------- #
# ---------------------------------- MAIN ---------------------------------- #

snake = Snake(3)
food = Food()
scoreboard = ScoreBoard()

# Listen to keypress
screen.listen()
screen.onkey(fun=snake.up,key='w')
screen.onkey(fun=snake.left,key='a')
screen.onkey(fun=snake.down,key='s')
screen.onkey(fun=snake.right,key='d')

game_over = False
while not game_over:
    # Refresh Screen
    screen.update()
    time.sleep(0.075)

    # Move Snake
    snake.move_forward(20)

    # Check Food Collision
    if snake.head.distance(food.pos()) <= 20:
        food.refresh()
        snake.extend_body()
        scoreboard.add_score()

    # Wall Collision
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        game_over = True
        scoreboard.game_over()
    
    # Tail collision
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) <= 10:
            game_over = True
            scoreboard.game_over()






















screen.exitonclick()