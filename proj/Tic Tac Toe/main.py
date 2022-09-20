from tabulate import tabulate
from copy import deepcopy

ROW = 3
COLUMN = 3

class TicTacToe:
    
    P1_SYMBOL = 'X'
    P2_SYMBOL = 'O'
    
    def __init__(self) -> None:
        self.game_table = self.create_table()
        pass
    
    def create_table(self):
        return [['#' for _ in range(ROW)] for i in range(COLUMN)]
        
    def __str__(self):
        display_table = deepcopy(self.game_table)
        for i in range(len(display_table)):
            display_table[i].insert(0, i)
        return tabulate(display_table, headers=[i for i in range(COLUMN)], tablefmt="fancy_grid", numalign="left")
    
    def change_cell(self, symbol: str, xy: tuple):
        self.game_table[xy[0]][xy[1]] = symbol
    
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
    

def play_game():
    new_game = TicTacToe()