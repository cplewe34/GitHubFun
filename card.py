import random 

#list for the suits and then dictionary for the rest of the cards and thier values. 
suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
rank_values = { "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":13, "Ace":14 }   

class Card:

    #the initializatoin for the cards with the suit rank and value. 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank_values[rank]

    #this is the string for each object in this class
    def __str__(self):
        return(f"{self.rank} of {self.suit}")

    #tells wether one card is higher than another
    def beats(self, other):
        if self.value > other.value:
            return True
        else: 
            return False

    #tells wether or not the cards have the same value. 
    def tie(self, other):
        if self.value == other.value:
            return True
        else:
            return False
        


class Deck:
    #rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  

    #initialization for a deck
    def __init__(self):
        self.card_list = []

    # this method builds a deck
    def build(self):
        for rank in rank_values:
            for i in suit:
                self.card_list.append(Card(i,rank))

    #this method shuffles a deck
    def shuffle(self):
        random.shuffle(self.card_list)

    #this method deals a card in the deck
    def deal(self):
        if len(self.card_list) == 0:
            return None
        else:
            return self.card_list.pop(0)

    #this method adds cards to the botton of a deck
    def add_card(self, card_in):
        self.card_list.append(card_in)

    #shows how many cards are in the deck
    def __len__(self):
        return len(self.card_list)

    #tells weather or not the deck is empty
    def is_empty(self):
        if  len(self.card_list) == 0:
            return True
        else:
            return False
