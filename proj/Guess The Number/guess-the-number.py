import random
from replit import clear

def difficult_selector(choice: str) -> str:
    if choice == 'e':
        return 15
    elif choice == 'm':
        return 10
    elif choice == 'h':
        return 5
    else:
        choice = input("invalid input, try again (e/m/h): ")
        return difficult_selector(choice)

if __name__ == "__main__":
    print("Welcome to the guessing game!")
    endpoint = (1,100)
    secret_num = random.randint(endpoint[0], endpoint[1])
    print(f"Im thinking a number between {endpoint[0]} and {endpoint[1]}")

    amount_of_lives = difficult_selector(input("Choose a difficulty (e, m, h): "))
    clear()

    guess = -1
    while guess != secret_num and amount_of_lives > 0:
        print(f"You have {amount_of_lives} of guesses left")
        guess = int(input("Make a guess: "))
        amount_of_lives -= 1
        if guess > secret_num:
            print("Too High")
        elif guess < secret_num:
            print("Too low")
    
    print(f"The number is {secret_num}")
    
    if guess == secret_num:
        print("You win")
    elif amount_of_lives <= 0:
        print("You lose")