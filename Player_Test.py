from Player import *

# Test the Player class
if __name__ == "__main__":
    manual_player = ManualPlayer()
    random_player = RandomPlayer()
    dealer = Dealer()

    # [Dealer, Player 1, Player 2, ...]
    players = [dealer, manual_player, random_player]

    game = Game(len(players), decks=1)
    game.play_game(players)
    
    print(game.winner)