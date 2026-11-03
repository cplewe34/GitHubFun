from card import deck
from player import player

def play_round(player1, player2):
    #Play one round (including any wars). Returns (winner, was_war)
    card1 = player1.draw_card()
    card2 = player2.draw_card()
    print(f"{player1} drew the {card1}.")
    print(f"{player2} drew the {card2}.")

    pot = [card1, card2]  # every card played this round

    # Keep going to war until the cards are different.
    while card1 == card2:
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

        card1 = player1.draw_card()
        card2 = player2.draw_card()
        print(f"{player1} drew the {card1}.")
        print(f"{player2} drew the {card2}.")
        pot.extend([card1, card2])

    winner = player1 if card1 > card2 else player2
    winner.collect_cards(pot)
    return winner, len(pot) > 2

def main():
    print("This is War! Welcome, soldier.")

    # Two separate decks, each shuffled, one per player.
    deck1 = deck()
    deck2 = deck()
    deck1.shuffle()
    deck2.shuffle()
    player1 = player("Player 1", deck1.deal_all())
    player2 = player("Player 2", deck2.deal_all())

    auto = False
    round_number = 0

    while player1.has_cards() and player2.has_cards():
        round_number += 1
        winner, was_war = play_round(player1, player2)
        print(f"{winner} wins the {'war' if was_war else 'round'}!")

        print(f"{player1} has {player1.count_cards()} cards.")
        print(f"{player2} has {player2.count_cards()} cards.")

        if not auto:
            input("Press Enter to continue to the next round...")

    overall_winner = player1 if player1.has_cards() else player2
    print(f"{overall_winner} wins the game!")
        