import random
from replit import clear

def setup_cards() -> list:
    """ Returns a shuffled deck of cards """
    card_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
    for i in range(8):
        random.shuffle(card_deck)
    return card_deck

def csum(deck: list) -> int:
    """ Returns the sum of all cards in the given deck

        Jack, Queen and King cards are worth 10 each.
        Ace card is worth either 1 or 11 according to result
    """
    card_map = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    new_cards = []
    for card in deck:
        new_cards.append(card_map[card])
    res = sum(new_cards)
    for _ in range(deck.count(11)):
        if res > 21:
            res -= 11 - 1 # replaces 'A' with 1 instead of 11
    return res

def win_check(player_sum, comp_sum):
    if player_sum == comp_sum:
        return "Drew"
    if player_sum > 21 and comp_sum > 21:
        return "Drew"
    elif player_sum == 21 or comp_sum > 21:
        return "Win"
    elif comp_sum == 21 or player_sum > 21:
        return "Lose"
    elif player_sum > comp_sum:
        return "Win"
    elif comp_sum > player_sum:
        return "Lose"

def play_game():
    clear()
    print("-- BLACK JACK --")
    game_cards = setup_cards()
    
    player_cards = [game_cards.pop()]
    computer_cards = [game_cards.pop()]

    game_over = False
    while not game_over:
        print(f"Your cards: {player_cards}")
        print(f"Computers first card: {computer_cards[0]}")

        hit_stand = input("Do you want to hit or stand (h/s): ")
        clear()

        if csum(computer_cards) < 17:
            computer_cards.append(game_cards.pop())
        
        if hit_stand == 'h':
            player_cards.append(game_cards.pop())
        elif hit_stand == 's':
            while csum(computer_cards) < 17:
                computer_cards.append(game_cards.pop())
        
        player_score = csum(player_cards)
        comp_score = csum(computer_cards)
        
        if hit_stand == 's' or player_score == 21 or player_score > 21 or comp_score == 21 or comp_score > 21:    
            game_over = True

    is_win = win_check(player_score, comp_score)
                    
    print(f"Your final hand: {player_cards} = {csum(player_cards)}")
    print(f"Computers final hand: {computer_cards} = {csum(computer_cards)}")
    print(f"You {is_win}!")
    
if __name__ == "__main__":
    play = input("Do you want to play Blackjack (y/n): ")
    while play == 'y':
        play_game()
        play = input("Do you want to continue playing (y/n): ")