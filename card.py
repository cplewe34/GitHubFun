import random 

suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
rank_values = { "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":13, "Ace":14 }   

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank_values[rank]

    def __str__(self):
        return(f"{self.rank} of {self.suit}")

    def beats(self, other):
        if self.value > other.value:
            return True
        else: 
            return False

    def tie(self, other):
        if self.value == other.value:
            return True
        else:
            return False
        


class Deck:
    #rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  

    def __init__(self):
        self.card_list = []

    def build(self):
        for rank in rank_values:
            for i in suit:
                self.card_list.append(Card(i,rank))

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) == 0:
            return None
        else:
            return self.card_list.pop(0)

    def add_card(self, card_in):
        self.card_list.append(card_in)

    def __len__(self):
        return len(self.card_list)
    
    def is_empty(self):
        if  len(self.card_list) == 0:
            return True
        else:
            return False
