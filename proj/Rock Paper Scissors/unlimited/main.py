from RockPaperScissorUnlimited import RPSUnlimited
from rich.console import Console
from copy import deepcopy
import time
import math
import os

class RPSElimination(RPSUnlimited):
    
    rounds = 0
    check = ''
    delay = 3

    def __init__(self, user_amount: int, bot_amount: int) -> None:
        super().__init__(user_amount, bot_amount)
        self.player_pool = [player for player in self.players.keys()]
        self.console = Console()
        
    def mainloop(self):
        self.clear_screen()
        while len(self.player_pool) > 1:
            self.rounds += 1
            time.sleep(self.delay)
            self.clear_screen()
            self.console.print(f"Round {self.rounds}: {self.player_pool}\n")
            time.sleep(self.delay/2)
            self.clear_screen()
            
            self.get_player_choices()
            self.clear_screen()
            self.evaluate_choices()
            self.eliminate_players()
            
            if not self.user_in_pool() and len(self.player_pool) > 1:
                if self.check == '':
                    self.check = input("All players are eliminated, Would you like to let the bots finish (y/n): ")
                
                if self.check == 'y':
                    continue
                else:
                    return
        
        time.sleep(self.delay)
        self.clear_screen()
        print(f"The winner is {self.return_winner()}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    def get_player_choices(self):
        for player in self.player_pool:
            if self.players[player]['is_bot'] == True:
                self.bot_choice(player)
            elif self.players[player]['is_bot'] == False:
                self.user_choice(player)
                self.clear_screen()
    
    def evaluate_choices(self):
        all_choices = [self.players[player]['current_choice'] for player in self.player_pool]

        for player in self.player_pool:
            for choice in all_choices:
                self.players[player]['points'] += self.compare_player_choice(self.players[player]['current_choice'], choice)
    
    def eliminate_players(self):
        pool = deepcopy(self.player_pool)
        highest_point = max([self.players[player]['points'] for player in pool])
        lowest_points = min([self.players[player]['points'] for player in pool])
        threshold = math.floor((highest_point+lowest_points)/2)
        print(f"Players with less than {threshold} points are eliminated!\n")
        time.sleep(1)
        for player in pool:
            state = self.players[player]
            if state['points'] >= threshold:
                self.console.print(f"[magenta]'{player}'[/magenta] chose [magenta]{state['current_choice']}[/magenta] and now has [magenta]{state['points']}[/magenta] points! They have made it to the [green]next rounds[/green]")
            elif state['points'] < threshold:
                self.console.print(f"[magenta]'{player}'[/magenta] chose [magenta]{state['current_choice']}[/magenta] and now has [magenta]{state['points']}[/magenta] points! They are [red]eliminated[/red]")
                self.player_pool.remove(player)

    def user_in_pool(self):
        """ Checks if the player pool consists of at least one user """
        for player in self.player_pool:
            state = self.players[player]
            if state['is_bot'] == False:
                return True
        return False
        
    def return_winner(self):
        if len(self.player_pool) != 0:
            return self.player_pool[0]
        else:
            return "-"    

def main():
    os.system('cls')
    game = RPSElimination(user_amount=int(input("How much players: ")), bot_amount=int(input("How much bots: ")))
    
    add_choices = input("Do you want to add any choice (y/n): ")
    while add_choices == 'y':
        game.add_new_choice()
        add_choices = input("Another choice? (y/n): ")
    game.mainloop()

if __name__ == "__main__":
    main()
