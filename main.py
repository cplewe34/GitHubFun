# main.py
# This file runs the card game War.
# It uses the deck class (from card.py) and the player class (from player.py).

import random
from card import Deck
from player import Player


def play_round(player1, player2):
    #Play one round (including any wars). Returns (winner, was_war)
    card1 = player1.draw_card()
    card2 = player2.draw_card()
    print(f"{player1} drew the {card1}.")
    print(f"{player2} drew the {card2}.")

    pot = [card1, card2]  # every card played this round

    # Keep going to war until the cards are different.
    while card1.tie(card2):
        print("War!")

        # A player with no cards left cannot fight the war and loses it.
        if not player1.has_cards():
            print(f"{player1} has no cards left for the war!")
            player2.collect_cards(pot)
            return player2, True
        if not player2.has_cards():
            print(f"{player2} has no cards left for the war!")
            player1.collect_cards(pot)
            return player1, True

        # Each player draws a card for the war.
        card1 = player1.draw_card()
        card2 = player2.draw_card()
        print(f"{player1} drew the {card1}.")
        print(f"{player2} drew the {card2}.")
        # Adds new cards to the pot for the war.
        pot.extend([card1, card2])

    # Determine the winner of the round and give them all the cards in the pot.
    winner = player1 if card1.beats(card2) else player2
    random.shuffle(pot)  # Shuffle the pot before giving it to the winner.
    winner.collect_cards(pot)
    return winner, len(pot) > 2

def main():
    print("This is War! Welcome, soldier.")

    # Two separate decks, each shuffled, one per player.
    deck1 = Deck()
    deck2 = Deck()
    deck1.build() 
    deck2.build() 
    deck1.shuffle()
    deck2.shuffle()
    player1 = Player("Player 1", deck1)
    player2 = Player("Player 2", deck2)

    # Play rounds until one player has all the cards.
    choice = input("Type 'a' to auto-play, or press Enter to play round by round: ")
    auto = choice.strip().lower() == "a"
    round_number = 0

    # Play rounds until one player has all the cards.
    while player1.has_cards() and player2.has_cards():
        round_number += 1
        print(f"\n--- Round {round_number} ---")
        winner, was_war = play_round(player1, player2)
        print(f"{winner} wins the {'war' if was_war else 'round'}!")

        print(f"{player1} has {player1.count_cards()} cards.")
        print(f"{player2} has {player2.count_cards()} cards.")

        if not auto:
            input("Press Enter to continue to the next round...")

    # Determine the overall winner and print the result.
    overall_winner = player1 if player1.has_cards() else player2
    print(f"\n{overall_winner} wins the game after {round_number} rounds!")

# Run the main function if this file is executed directly.
if __name__ == "__main__":
    main()

