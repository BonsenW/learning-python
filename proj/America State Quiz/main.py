import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

blank_states_img = 'blank_states_img.gif'
screen.addshape(blank_states_img)

turtle.shape(blank_states_img)
screen.tracer(0)

# ----------------------------- text turtle ----------------------------- #
text = turtle.Turtle()
text.penup()
text.hideturtle()

# ------------------------------ main game ------------------------------ #
state_data = pd.read_csv("50_states.csv")
state = state_data['state']


guess_counter = 0
remaining_states = state.to_list()
while len(remaining_states) > 0:
    player_guess = screen.textinput(title=f"{50-len(remaining_states)}/50 states", prompt="Guess a state (type exit to exit)").capitalize()
    guess_counter += 1

    if player_guess == 'Exit':
        break

    if player_guess in remaining_states:
        x_cor, y_cor = int(state_data[state == player_guess]['x']), int(state_data[state == player_guess]['y'])
        text.goto(x_cor, y_cor)
        text.write(player_guess)
        remaining_states.pop(remaining_states.index(player_guess))

    screen.update()

if len(remaining_states) <= 0:
    print(f"Congratulation, you won the state game, it took you {guess_counter} tries to guess 50 states")
else:
    states_to_learn = pd.Series(remaining_states) 
    states_to_learn.to_csv("states-to-learn.csv")
