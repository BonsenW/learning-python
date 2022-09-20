from random import choice

CHOICES = {
    'r' : "rock",
    'p' : "paper",
    's' : "scissor"
}

def get_user_choice():
    player_choice = input("(R)ock | (P)aper | (S)cissor\n").lower()

    if player_choice not in CHOICES.keys():
        print("Invalid Choice")
        return get_user_choice()
    
    return player_choice

def get_computer_choice():
    ai_choice = choice(list(CHOICES.keys()))

    return ai_choice

def check_game_state(p_choice, c_choice):
    state = ''
    if p_choice == c_choice:
        state = 'draw'
    elif (p_choice == 'r' and c_choice == 's') or (p_choice == 'p' and c_choice == 'r') or (p_choice == 's' and c_choice == 'p'):
        state = 'win'
    else:
        state = 'lose'
    
    return state

def point_counter(p_points, c_points, game_state):
    if game_state == 'win':
        p_points += 1
    elif game_state == 'lose':
        c_points += 1
    
    return (p_points, c_points)

def check_winner(p_points, c_points):
    if p_points > c_points:
        print("You win!")
    elif p_points < c_points:
        print("You lose!")
    else:
        print("Draw!!")

def play_game():
    print("-------     START GAME     -------")
    print("-------                    -------\n")
    amount_of_games = int(input("BEST OUT OF: "))
    game_points = (0,0)

    while amount_of_games > 0:
        player_choice = get_user_choice()
        ai_choice = get_computer_choice()
        game_state = check_game_state(player_choice, ai_choice)
        game_points = point_counter(game_points[0], game_points[1], game_state)

        print(f"{CHOICES[player_choice]} vs {CHOICES[ai_choice]}, you {game_state}")
        print(f"{game_points[0]} - {game_points[1]}\n")
        
        if game_state != 'draw':
            amount_of_games -= 1

        if (game_points[0] + amount_of_games) < game_points[1] or (game_points[1] + amount_of_games) < game_points[0]:
            break

    check_winner(game_points[0], game_points[1])

if __name__ == "__main__":
    play_game()
