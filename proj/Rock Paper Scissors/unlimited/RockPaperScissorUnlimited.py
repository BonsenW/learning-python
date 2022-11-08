import random
import json
import os

name_file = f"{os.getcwd()}\\unlimited\\names.txt"
choice_file = f"{os.getcwd()}\\unlimited\\choice.json"

class RPSUnlimited():

    players = {} # keys: name, points, current_choice, is_bot
    
    def __init__(self, user_amount: int, bot_amount: int) -> None:
        self.user_amount = user_amount
        self.bot_amount = bot_amount
        self.setup_users()
        self.setup_bots()
        
        self.choices = self.get_choice()
        
    def evaluate_choices(self):
        all_choices = [self.players[player]['current_choice'] for player in self.players.keys()]

        for player in self.players.keys():
            for choice in all_choices:
                self.players[player]['points'] += self.compare_player_choice(self.players[player]['current_choice'], choice)
        
    def compare_player_choice(self, a, b):
        b_properties = self.choices[b]
        # if the two choices are equal to each other or they beat each other, then draw (0)
        if a == b or (a in b_properties['beaten_by'] and a in b_properties['beats']):
            return 0
        # if choice a beats b, then win (+1)
        elif a in b_properties['beaten_by']:
            return +1
        # if choice a is beaten by b, then lose (-1)
        elif a in b_properties['beats']:
            return -1
        else:
            return 0
             
    def get_player_choices(self):
        for player in self.players.keys():
            if self.players[player]['is_bot'] == True:
                self.bot_choice(player)
            elif self.players[player]['is_bot'] == False:
                self.user_choice(player)

    def user_choice(self, user_name):
        # Create the input string from the choices avaliable
        options = '|'.join([f" {choice} " for choice in self.choices.keys()])
        user_choice = input(f"{user_name}: {options}: ").lower()

        # Validate the choice
        if user_choice not in self.choices.keys():
            print("Invalid Choice")
            return self.user_choice(user_name=user_name)
    
        # Save the choice into the player dictionary
        self.players[user_name]['current_choice'] = user_choice
    
    def bot_choice(self, bot_name):
        bot_choice = random.choice(list(self.choices.keys()))
        self.players[bot_name]['current_choice'] = bot_choice       
    
    def setup_users(self):
        i = 0
        while i < self.user_amount:
            user_name = input(f"Player {i+1}'s name: ")
            if user_name in self.players:
                print("Invalid, name already used.")
                continue
            points = 0
            is_bot = False
            self.players[user_name.capitalize()] =  { 'name': user_name, 'points' : points, 'current_choice' : None, 'is_bot' : is_bot }
            i += 1

    def setup_bots(self):
        for i in range(self.bot_amount):
            bot_name = self.get_random_name()
            points = 0
            is_bot = True
            self.players[bot_name.capitalize()] =  { 'name' : bot_name, 'points' : points, 'current_choice' : None, 'is_bot' : is_bot }
    
    def add_new_choice(self):
        name = input("What is the name of the new choice (names can override): ").lower()
        beats = input("What does it beat? (Check spelling, seperate by comma with no space): ").lower().split(',')
        beaten_by = input("What is it beaten by? (Check spelling, seperate by comma with no space): ").lower().split(',')
        
        new_value = {
            name : { "beats" : beats, "beaten_by" : beaten_by},
        }
        
        current_choices = self.get_choice()
        
        for value in beats:
            try:
                if name not in current_choices[value]['beaten_by']:
                    current_choices[value]['beaten_by'].append(name)
            except KeyError:
                current_choices[value] = { "beats" : [], "beaten_by" : [name]}

        for value in beaten_by:
            try:
                if name not in current_choices[value]['beats']:
                    current_choices[value]['beats'].append(name)
            except KeyError:
                current_choices[value] = { "beats" : [name], "beaten_by" : []}
            
        
        with open(choice_file, 'w') as file:
            current_choices.update(new_value)
            json.dump(current_choices, file, indent=4)
        self.choices = self.get_choice()
        print(f"{name} added!")
    
    def get_choice(self):
        with open(choice_file, 'r') as file:
            current_choices: dict = json.load(file)
        return current_choices
    
    def get_random_name(self):
        names = []
        with open(name_file, 'r') as file:
            for line in file.readlines():
                names.append(line.strip())
        return random.choice(names)
        
    def get_player_names(self):
        for player in self.players.keys():
            if self.is_bot(player):
                yield f"{player} (Bot)"
            else:
                yield f"{player}"
    
    def clear_screen(self):
        os.system('cls')
    
    def is_bot(self, name):
        return self.players[name]['is_bot']
    
    def validate_integers(self, *values):
        for value in values:
            assert type(value) == int, f"{value} is not an integer value."

if __name__ == "__main__":
    pass    