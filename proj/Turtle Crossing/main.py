from turtle import Screen, screensize
from game_objects import BabyTurtle, Car
from level_manager import LevelManager
import time
import random

SCREEN_BUFFER = 25
MAX_CARS = 30
TIME_BTW_SPAWNS = 5
DISTANCE_BUFFER = 22

# ---------------------------- screen setup ---------------------------- #
game_screen = Screen()
game_screen.setup(width=600,height=600)
game_screen.colormode(255)
game_screen.bgcolor('white')
game_screen.tracer(0)

x_boundary = game_screen.window_width()/2 + SCREEN_BUFFER
y_boundary = game_screen.window_height()/2 - SCREEN_BUFFER

# ---------------------------- turtle setup ---------------------------- #
player = BabyTurtle((0, -y_boundary))
level = LevelManager((-(x_boundary-(4*SCREEN_BUFFER)), y_boundary - SCREEN_BUFFER))

# ---------------------------- main code ---------------------------- #
game_screen.listen()

current_car_counter = 0
counter = 0
game_over = False
while not game_over:
    game_screen.update()
    time.sleep(0.05)

    # input checks
    game_screen.onkey(fun=player.move_forward, key='w')

    # instantiate car
    if counter <= 0 and current_car_counter < MAX_CARS:
        car_position = (x_boundary, random.randint(-y_boundary, y_boundary))
        car = Car(car_position)
        current_car_counter += 1
        counter = TIME_BTW_SPAWNS
    else:
        counter -= 1

    # move car
    for t in game_screen.turtles():
        if type(t) == Car:
            if t.xcor() < -x_boundary:
                car_position = (x_boundary, random.randint(-y_boundary, y_boundary))
                t.set_newpos(car_position)
            else:
                t.move_forward()

            # player-car collision
            if player.distance(t) <= DISTANCE_BUFFER:
                level.game_over()
                time.sleep(1)
                game_screen.bye()


    # if at the top
    if player.ycor() >= y_boundary:
        level.increase_level()
        level.update_scoreboard()
        
        for t in game_screen.turtles():
            if type(t) == Car:
                t.increase_speed()
        player.reset_position()
    















game_screen.update()
game_screen.exitonclick()