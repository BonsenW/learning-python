from TicTacToe import TicTacToe
import os

def main():
    os.system('cls')
    replay = 'y'
    try:
        while replay == 'y':
            grid_size = int(input("Grid Size: "))
            player_amount = int(input("Player Amount: "))
            game = TicTacToe(grid_size=grid_size, player_amount=player_amount)
            game.main_loop()
            replay = input("Play again? (y/n): ")
            game.clear_terminal()
    except (AssertionError, ValueError) as e:
        print(f"\n{e}\n\nRestarting...\n\n")
        main()
        
if __name__ == "__main__":
    main()