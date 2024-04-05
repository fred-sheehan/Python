# A slightly more complete version of the 100 Days of Code blackjack
# python file I completed on Day 11. This version includes all the
# other enhancements I added to that file, plus some extras!
# still not perfect but getting there, enjoy! - Fred
from blackjack_fred_logo import logo
import random
import os

def clear():
    os.system('cls||clear')

def show_logo():
    print(logo)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.stay = False

    def reset(self):
        self.hand = []
        self.score = 0
        self.stay = False

    def draw_card(self, deck):
        card = deck.pop()
        self.hand.append(card)
        self.score += card
        if self.score == 21 and len(self.hand) == 2:
            print(f"{self.name} has a Blackjack with a score of {self.score}")

    def show_hand(self, show_all_cards=False):
        if show_all_cards:
            print(f"{self.name}'s hand: {self.hand} (Sum: {self.score})")
        else:
            if self.name == "Dealer":
                print(f"Dealer's hand: [{self.hand[0]}, ?]")
            else:
                if self.score == 21 and len(self.hand) == 2:
                    print(f"{self.name}'s hand: {self.hand} (Blackjack!!)")
                else:
                    print(f"{self.name}'s hand: [{self.hand[0]}, ?]")

def create_deck():
    deck = []
    for _ in range(4):
        for i in range(2, 11):
            deck.extend([i]*4)
        deck.extend([10]*12)
    random.shuffle(deck)
    return deck

def check_winner(players, dealer):
    for player in players:
        if player.score == 21 and len(player.hand) == 2:
            print(f"{player.name} has a Blackjack with a score of {player.score}")

    if dealer.score == 21 and len(dealer.hand) == 2:
        print("Dealer has a Blackjack with a score of 21")

    for player in players:
        if player.name != "Dealer":  # Skip the dealer for individual outcomes
            if player.score == 21 and len(player.hand) == 2:
                continue  # Skip displaying the player if they have a Blackjack
            if player.score > 21:
                print(f"{player.name} busts with a score of {player.score}")
            elif player.score <= 21 and dealer.score > 21:
                print(f"{player.name} wins with a score of {player.score} (Dealer bust)")
            elif player.score <= 21 and player.score > dealer.score:
                print(f"{player.name} wins with a score of {player.score}")
            elif player.score == dealer.score:
                print(f"{player.name} ties with the dealer with a score of {player.score}")
            else:
                print(f"{player.name} loses with a score of {player.score}")

    if dealer.score <= 21:
        print(f"Dealer's final score: {dealer.score}")

def blackjack():
    deck = []

    play_again = True
    while play_again:
        clear()
        show_logo()

        # Create and shuffle a new deck only if the deck is empty
        if not deck:
            deck = create_deck()

        players = []
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            name = input(f"Enter player {i + 1}'s name: ")
            players.append(Player(name))

        players.append(Player("Dealer"))

        while deck:
            for player in players:
                player.reset()

            print("\nStarting a new round...")
            for _ in range(2):
                for player in players:
                    if not deck:
                        print("\nThe deck is empty. Please start a new round with a new deck.")
                        break
                    player.draw_card(deck)

            random.shuffle(deck)

            players[-1].show_hand()
            for player in players[:-1]:
                player.show_hand(True)

            for player in players[:-1]:
                while not player.stay and player.score < 21:
                    player.show_hand(True)
                    if player.name == "Dealer":
                        if player.score < 17:
                            player.draw_card(deck)
                        else:
                            player.stay = True
                    else:
                        action = input(f"{player.name}, do you want to hit or stay? (h/s): ").lower()
                        if action == 'h':
                            if not deck:
                                print("\nThe deck is empty. Please start a new round with a new deck.")
                                break
                            player.draw_card(deck)
                            player.show_hand(True)
                            if player.score >= 21:
                                break
                        elif action == 's':
                            player.stay = True

                if not deck:
                    break

                if player.score == 21 and len(player.hand) == 2:
                    print(f"{player.name} has a Blackjack with a score of {player.score}")
                else:
                    print(f"{player.name} finishes with a score of {player.score}")

            if not deck:
                break

            player = players[-1]
            while player.score < 17:
                player.draw_card(deck)
                player.show_hand(True)

            print("\nDealer's hand:")
            player.show_hand(True)

            if not deck:
                break

            print("\nGame Results:")
            check_winner(players[:-1], player)

            response = input("\nDo you want to play again with a new deck? (y/n): ").lower()
            if response != 'y':
                play_again = False
                break

    print("\nThanks for playing!")

clear()
show_logo()
blackjack()
