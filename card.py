# Bowen and Sam here. We used placeholder names in my code for the functions and classes you guys will make.
# "deck" is the main class we used to import
# we used a placeholder for a "shuffle" function, and a "deal_all" function 
import random 


class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return(f"{self.rank} of {self.suit}")

#check with others about tie
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
    suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
    rank = { "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":13, "Ace":14 }     

    def __init__(self):
        self.card_list = []

    def build(self):
        for rank in self.rank:
            for suit in self.suit:
                self.card_list.append(Card(self.rank, self.suit))

    def shuffle(self):
        random.self.card_list

    def deal(self):
        
