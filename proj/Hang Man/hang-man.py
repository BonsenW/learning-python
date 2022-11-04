from random import choice
from tabulate import tabulate

STAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def print_heading(string: str):
    """ Prints a fancy heading """
    print(tabulate([string], tablefmt='fancy_grid'))
    
def word_generator(file_name: str) -> str:
    """ Generates a random word from a word list file """
    assert type(file_name) == str, "The file is invalid! Error: Not a string"
    with open(file_name, 'r') as words:
        return choice(words.readlines()).strip()

def track_secret_word(secret: str, chars: list = []) -> str:
    """ Compares a list of characters against a secret word returning the state of the words

        If a character is in the secret word, the character replaces the underscore
    """
    state = ['_'] * len(secret)
    for char in chars:
        if char not in secret:
            continue
        for i in range(len(secret)): 
            if char == secret[i] and state[i] == '_':
                state[i] = char
    return ''.join(state)

def main():
    secret_word = word_generator(r"hangman_words.txt")
    lives = 6
    guess_list = []
    current_state = track_secret_word(secret_word, guess_list)
    print_heading("HANGMAN")
    print_heading(current_state)

    while current_state != secret_word and lives > 0:
        guess_list.append(input(f"Guess a letter: "))

        old_state = current_state
        current_state = track_secret_word(secret_word, guess_list)
        if old_state == current_state:
            lives -= 1
            print(f"\nLost 1 life! {STAGES[-lives]}")
        print_heading(current_state)
        print(','.join(guess_list), end='\n\n')
    
    if lives > 0:
        print(f"You win, secret word is: {secret_word}")
    else:
        print(f"You lose, secret word is: {secret_word}")

if __name__ == "__main__":
    main()