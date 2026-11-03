from card import deck

class player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = deck

    def draw_card(self):
        return self.hand.draw_card()
    
    def collect_cards(self, deck):
        self.hand.collect_cards(deck)

    def count_cards(self):
        return self.hand.count_cards()

    def has_cards(self):
        return not self.hand.is_empty()

    def __str__(self):
        return f"{self.name} {self.count_cards()} cards."

    