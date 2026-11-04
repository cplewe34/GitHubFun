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
        return self.hand.deal()
    
    def collect_cards(self, cards):
        # Collects cards from a deck and adds them to the player's hand.
        for card in cards:
            self.hand.add_card(card)

    def count_cards(self):
        # Returns the number of cards in the player's hand.
        return len(self.hand)

    def has_cards(self):
        # Returns True if the player has cards left in their hand, False otherwise.
        return not self.hand.is_empty()

    def __str__(self):
        # Returns a string representation of the player (their name).
        return f"{self.name}"

    