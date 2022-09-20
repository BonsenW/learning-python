from tabulate import tabulate
from copy import deepcopy
import os

ROW = 3
COLUMN = 3

class TicTacToe:

    def __init__(self) -> None:
        self.game_table = self.create_table()
            
    def create_table(self):
        return [[' ' for _ in range(ROW)] for i in range(COLUMN)]
    
    def get_player_input(self, symbol):
        print(f"Player {symbol}")
        x = int(input("Pick a x-pos: "))
        y = int(input("Pick a y-pos: "))
        self.change_cell(symbol, x, y)
        
    def change_cell(self, symbol: str, x: int, y:int):
        if (x > 3 or x < 0) or (y > 3 or y < 0) or self.game_table[x][y] != ' ':
            print("Invalid Position")
            return self.get_player_input(symbol)
        
        self.game_table[x][y] = symbol
         
    def check_win(self, symbol):
        # Horizontal Win
        is_hor_win = any([True for row in self.game_table if row.count(symbol) == 3])

        # Vertical Win
        vertical_list = [[self.game_table[j][i] for j in range(len(self.game_table[i]))] for i in range(len(self.game_table))]
        is_ver_win = any([True for row in vertical_list if row.count(symbol) == 3])
        
        # Diagonal Win
        diagonal_list = [self.game_table[i][i] for i in range(len(self.game_table))]
        diagonal_list_inv = [self.game_table[i][-(i+1)] for i in range(len(self.game_table[::]))]
        
        return is_hor_win or is_ver_win or diagonal_list.count(symbol) == 3 or diagonal_list_inv.count(symbol) == 3
    
    def __str__(self):
        display_table = deepcopy(self.game_table)
        for i in range(len(display_table)):
            display_table[i].insert(0, i)
        return tabulate(display_table, headers=[i for i in range(COLUMN)], tablefmt="fancy_grid", numalign="left")

def play_game():
    game = TicTacToe()    
    symbols = ['X', 'O']
    
    print("----- TIC TAC TOE -----")
    game_over = False
    while not game_over:
        for symb in symbols:
            print(game)
            game.get_player_input(symb)
            os.system('CLS')
            if game.check_win(symb):
                game_over = True
                winner = symb
                break
    
    print(game)
    print(f"Player {winner} wins!")
    
if __name__ == "__main__":
    
    replay = 'y'
    while replay == 'y':
        play_game()
        replay = input("Play again? (y/n): ")
        os.system('CLS')