import random as rand
from Game import Game

# Dealer Class uses a basic strategy of hitting until the value 
# of the hand is 17 or greater
class Dealer: 
    def __init__(self):
        # self.hand = []
        self.value = 0
        self.game = Game()
    
    def get_move(self, game, hand):
        self.value = game.calculateScore(hand)
        if self.value < 17:
            return "hit"
        else:
            return "stand"
        
# ManualPlayer Class allows the user to input their move
class ManualPlayer:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.game = Game()
    
    def get_move(self, game, hand):
        self.value = game.calculateScore(hand)
        self.hand = hand
        while True:
            move = input("Enter 'h' to hit or 's' to stand: ").lower()
            if move == 'h':
                return "hit"
            elif move == 's':
                return "stand"
            else:
                print("Invalid move. Please try again.")
    
# RandomPlayer Class randomly selects a move
# hit or stand with equal probability (50/50)
class RandomPlayer:
    def __init__(self):
        self.hand = []
        self.value = 0

    def get_move(self, game, hand):
        self.value = game.calculateScore(hand)
        self.hand = hand
        if rand.random() < 0.5:
            return "hit"
        else:
            return "stand"

# CardCountingPlayer selects a move
# based on basic card counting strategy
class CardCountingPlayer:
    def __init__(self, num_decks):
        self.hand = []
        self.value = 0
        self.count = 0
        self.num_decks = num_decks

    def get_move(self, game, hand):
        self.hand = hand
        self.value = game.calculateScore(hand)
        self.update_count(hand)

        # Basic strategy based on count
        if self.count >= 2:
            # Bet more when count is high
            if self.value < 17 and game.board[0][1] < 7:
                return "hit"
            else:
                return "stand"
        else:
            # Bet less when count is low
            if self.value < 17:
                return "hit"
            else:
                return "stand"

    def update_count(self, hand):
        """Update the running card count based on the cards in the hand."""
        for card in hand:
            if card in [2, 3, 4, 5, 6]:
                self.count += 1
            elif card in [10, "J", "Q", "K", "A"]:
                self.count -= 1
        self.count = min(max(-self.num_decks * 10, self.count), self.num_decks * 10)
        
        
     
# Type of a Nearest Neighbor algorithm
# compares the players hand to the dealer and a 21 value 
# "classifies" the hand as hit or stand
class NearestNeighborPlayer:
    def __init__(self):
        pass

    def get_move(self, game, player_hand):
        player_value = game.calculateScore(player_hand)
        dealer_value = game.calculateScore(game.players[0])  # Assume only the dealer's visible card matters

        # Calculate the difference between the dealer's hand value and 21
        deaker_diff_to_21 = abs(dealer_value - 21)

        # Calculate the difference between the player's hand value and 21
        player_diff_to_21 = abs(player_value - 21)

        # If hitting would not cause the player to bust and getting closer to 21 than the dealer, hit
        if player_value < 21 and player_diff_to_21 > deaker_diff_to_21:
            return "hit"

        # Otherwise, stand
        return "stand"

# Minimax algorithm
# recursively simulates game with a depth cutoff (by default 3)
# decides which next move maximizes chances to win
class MinimaxPlayer:
    def __init__(self, depth=3, player_num=1):
        self.depth = depth
        self.player_num = player_num

    def get_move(self, game, player_hand):
        # Use minimax criteria here to determine the move
        return self.minimax(game.copy(), player_hand, self.depth)

    # recursive minimax algorithm with a set cutoff depth
    def minimax(self, game_state, move, depth):
        if depth == 0 or game_state.winner is not None:
            return self.evaluate(game_state)

        if game_state.turn == self.player_num:  # Player's turn (e.g., you in Blackjack)
            best_score = float('-inf')
            for next_move in self.get_legal_moves(game_state):
                if next_move == "hit":
                    game_state.hit()
                else:
                    game_state.stand()
                score = self.minimax(game_state, next_move, depth - 1)
                best_score = max(best_score, score)
            return best_score
        else:  # Opponent's turn (e.g., dealer in Blackjack)
            best_score = float('inf')
            for next_move in self.get_legal_moves(game_state):
                if next_move == "hit":
                    game_state.hit()
                else:
                    game_state.stand()
                score = self.minimax(game_state, next_move, depth - 1)
                best_score = min(best_score, score)
            return best_score

    def evaluate(self, game_state):
        player_score = game_state.calculateScore(game_state.board[self.player_num])
        dealer_card = game_state.calculateScore(game_state.board[0])  # Assume only the dealer's visible card matters
        remaining_cards = game_state.deck
        
        if player_score > 21:
            return -float('inf')  # Assign a very low score if player busts.
        
        # Base score is primarily the player's current hand value normalized.
        score = player_score - 21 if player_score <= 21 else -100  # Punish going over 21.

        # Modify score based on dealer's card.
        if dealer_card >= 7:
            score -= 5  # More risky situation if dealer has a strong card.
        elif dealer_card <= 6:
            score += 5  # Less risk if dealer might bust.

        # Adjust score based on the distribution of remaining cards.
        favorable_cards = sum(1 for card in remaining_cards if game_state.calculateScore([card]) + player_score <= 21)
        total_cards = len(remaining_cards)
        bust_probability = (total_cards - favorable_cards) / total_cards if total_cards else 1

        # Adjust score based on bust probability.
        score -= bust_probability * 10  # Penalize high risk of busting.
        return score

    def get_legal_moves(self, game_state):
        moves = ['stand', 'hit']  # Basic moves available in every situation.
        return moves