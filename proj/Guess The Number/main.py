from tabulate import tabulate
import random
import os

ENDPOINTS = (0, 1000)

def clear():
    os.system('cls')
    
def print_heading(string, end='\n'):
    print(tabulate([[string]], tablefmt='fancy_grid'), end=end)  

def print_list(heading, *args):
    print(tabulate([[string] for string in args], [heading], tablefmt='fancy_grid'), end='')    
  
def select_difficulty(choice: str) -> str:
    difficulty_selection = {
        'e' : 20,
        'm' : 15,
        'h' : 10
    }
    
    if choice not in difficulty_selection.keys():
        print_heading("Invalid Choice", end='')
        return select_difficulty(choice=input(""))
    return difficulty_selection[choice]

def generate_secret_number(x, y):
    """ Returns a random integer between x and y"""
    return random.randint(x, y)

def win_check(x, y):
    """ If x is equal to y, return True """
    return x==y

def limited_lives_mode(difficulty: dict):
    amount_of_lives = difficulty
    secret_number = generate_secret_number(*ENDPOINTS)
    
    player_guess = int(input(f"Guess A Number Between {ENDPOINTS[0]} and {ENDPOINTS[1]}: "))
    while player_guess != secret_number and amount_of_lives > 1:
        amount_of_lives -= 1
        if player_guess > secret_number:
            print("Too High\n")
        elif player_guess < secret_number:
            print("Too low\n")
        print(f"You have {amount_of_lives} guesses left")
        player_guess = int(input("Make another guess: "))
        
    print(f"\nThe number is {secret_number}")
    print("You win!!") if win_check(player_guess, secret_number) else print("You lose")
    return
    
def main():
    print_heading("Welcome to the guessing game!")
    print_list("Choose A Difficulty", "- Easy (E)", "- Medium (M)", "- Hard (H)")
    difficulty = select_difficulty(choice=input(" ").lower())
    clear()
    limited_lives_mode(difficulty)
    
if __name__ == "__main__":
    clear()
    main()
    input()
