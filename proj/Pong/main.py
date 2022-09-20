from turtle import Screen, turtlesize
from game_objects import Paddle, Paddle_AI, PaddleBall
import time

from score_board import ScoreBoard

SCREEN_BUFFER = 50
DISTANCE_BUFFER = 50

# ------------------------------------ screen ------------------------------------ #
game_screen = Screen()
game_screen.setup(width=800, height=600)
game_screen.bgcolor('black')
game_screen.title('Pong')
game_screen.tracer(0)

boundary_position = (game_screen.window_width()/2 - SCREEN_BUFFER, game_screen.window_height()/2 - SCREEN_BUFFER)

# ---------------------------------- gameobjects ---------------------------------- #
user_paddle = Paddle((boundary_position[0], 0))
ai_paddle = Paddle_AI((-boundary_position[0], 0), difficulty='easy')
game_ball = PaddleBall()
score_board = ScoreBoard()

# ----------------------------------- main loop ----------------------------------- #
game_screen.listen()

collision_buffer = 0
game_over = False
while not game_over:
    # game updates
    game_screen.update()
    time.sleep(0.025)

    # user inputs
    if user_paddle.ycor() > -boundary_position[1] and user_paddle.ycor() < boundary_position[1]:
        game_screen.onkeypress(fun=user_paddle.move_up, key='w')
        game_screen.onkeypress(fun=user_paddle.move_down, key='s')
    else:
        game_screen.onkeypress(fun=user_paddle.loop_around_up, key='w')
        game_screen.onkeypress(fun=user_paddle.loop_around_down, key='s')

    # ball movement
    game_ball.move()

    # ai tracking
    ai_paddle.track_ball(game_ball)

    # ball boundary detections
    if abs(game_ball.xcor()) > boundary_position[0]+DISTANCE_BUFFER:
        if game_ball.xcor() > boundary_position[0]+DISTANCE_BUFFER:
            # ai wins
            score_board.add_p1_score()
        elif game_ball.xcor() < -(boundary_position[0]+DISTANCE_BUFFER):
            # player wins
            score_board.add_p2_score()
        
        game_ball.reset_position()
        ai_paddle.reset_position()
        user_paddle.reset_position()

    # ball collisions
    collision_buffer += 1 if collision_buffer <= 0 else 0
    if collision_buffer > 0:
        # vertical collisions
        if (game_ball.ycor() >= boundary_position[1] or game_ball.ycor() <= -boundary_position[1]):
            game_ball.change_angle_dir()
            collision_buffer -= 10
        # paddle collision
        if (user_paddle.distance(game_ball) <= DISTANCE_BUFFER and game_ball.xcor() > boundary_position[0]/2) or (ai_paddle.distance(game_ball) <= DISTANCE_BUFFER and game_ball.xcor() < -boundary_position[0]/2):
            game_ball.change_velocity_dir()

            if game_ball.distance(user_paddle) < game_ball.distance(ai_paddle):
                relative_pos = game_ball.ycor() - user_paddle.ycor()
            else:
                relative_pos = game_ball.ycor() - ai_paddle.ycor()
                
            game_ball.setheading(-relative_pos)
            game_ball.increase_speed()

            collision_buffer -= 10



















game_screen.update()
game_screen.exitonclick()
