from tabulate import tabulate
from copy import deepcopy
import os

class TicTacToe:
    """ Tic Tac Toe is a game where a (generally) 3x3 grid is used to see who can be 
    the first person to get (generally) 3 matching symbols in a vertical, diagonal or horizontal row 
    
    This Tic Tac Toe allows for a modifiable grid size, player size, symbols and more!
    """
    
    def __init__(self, grid_size, player_amount) -> None:
        self.player_amount = player_amount
        self.grid_size = grid_size
        self.validate_grid_size()
        self.validate_player_amount()
        
        self.symbols = []
        for i in range(player_amount):
            self.get_symbols(i)
        
        self.game_table = self.create_table()
        
    def main_loop(self):
        """ The main game loop """
        print("----- TIC TAC TOE -----")
        game_over = False
        while not game_over:
            for symb in self.symbols:
                print(self)
                self.get_player_input(symb)
                self.clear_terminal()
                if self.check_win(symb):
                    game_over = True
                    winner = symb
                    break
        
        print(self)
        print(f"Player {winner} wins!")
    
    def get_symbols(self, player):
        """ Lets all user currently playing pick a symbol to represent their turn. """
        symb = input(f"Player {player+1}'s Symbol: ")
        if symb in self.symbols:
            print("Already taken symbol, retry!")
            self.get_symbols(player=player)
        else:
            self.symbols.append(symb)
                    
    def get_player_input(self, symbol):
        """ Retrieves player input """
        print(f"Player {symbol}")
        
        try:
            x = int(input("Pick a row →: "))
            y = int(input("Pick a column ↓: "))
            
            if (x >= self.grid_size or x < 0) or (y >= self.grid_size or y < 0) or self.game_table[x][y] != ' ':
                raise ValueError
            
        except ValueError:
            self.clear_terminal()
            print(self)
            print("Invalid Position\n")
            return self.get_player_input(symbol)
        
        self.change_cell(symbol, x, y)
        
    def change_cell(self, symbol: str, x: int, y:int):
        """ Changes a cell to a certain symbol """
        self.game_table[x][y] = symbol
         
    def check_win(self, symbol):
        """ Checks for a horizontal, vertical or diagonal win """
        # Horizontal Win
        is_hor_win = any([True for row in self.game_table if row.count(symbol) == self.grid_size])

        # Vertical Win
        vertical_list = [[self.game_table[j][i] for j in range(len(self.game_table[i]))] for i in range(len(self.game_table))]
        is_ver_win = any([True for row in vertical_list if row.count(symbol) == self.grid_size])
        
        # Diagonal Win
        diagonal_list = [self.game_table[i][i] for i in range(len(self.game_table))]
        diagonal_list_inv = [self.game_table[i][-(i+1)] for i in range(len(self.game_table[::]))]
        is_diag_win = diagonal_list.count(symbol) == self.grid_size or diagonal_list_inv.count(symbol) == self.grid_size
        
        return is_hor_win or is_ver_win or is_diag_win
    
    def create_table(self):
        """ Creates the game table """
        return [[' ' for _ in range(self.grid_size)] for i in range(self.grid_size)]
    
    def clear_terminal(self):
        """ Clears the terminal """
        os.system('cls')
    
    def validate_grid_size(self):
        """ Validates the size of the grid """
        assert self.grid_size >= 3, "Grid size needs to be at least 3 to play Tic Tac Toe"
        assert self.grid_size <= 25, "Grid size should be smaller than 25 for functional play"
    
    def validate_player_amount(self):
        """ Validates the amount of players """
        assert self.player_amount > 1, "Need more than 1 player to play Tic Tac Toe"
    
    def __str__(self):
        """ Displays the table when print is called """
        display_table = deepcopy(self.game_table)
        for i in range(len(display_table)):
            display_table[i].insert(0, i)
        return tabulate(display_table, headers=[i for i in range(self.grid_size)], tablefmt="fancy_grid", numalign="left")