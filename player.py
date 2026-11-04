# player.py
# This file defines a player in the game War.
# A player has a name and a pile of cards (their "hand").
# Most of the work is passed along to the deck class from card.py.
 
from card import Deck

# A player in the game War.
class player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = deck

    def draw_card(self):
        # Draws a card from the player's hand. Returns the card drawn.
        return self.hand.draw_card()
    
    def collect_cards(self, deck):
        # Collects cards from a deck and adds them to the player's hand.
        self.hand.collect_cards(deck)

    def count_cards(self):
        # Returns the number of cards in the player's hand.
        return self.hand.count_cards()

    def has_cards(self):
        # Returns True if the player has cards left in their hand, False otherwise.
        return not self.hand.is_empty()

    def __str__(self):
        # Returns a string representation of the player (their name).
        return f"{self.name}"

    