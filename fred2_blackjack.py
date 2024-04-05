# This code was written with the help of OpenAI
# and took only a few minutes, why did I waste so much time..
# I could have done this in a few minutes, but I spent hours on
# mine.. lolol
# It did take some prompt engineering and it was easier after
# struggling with mine for so long. I will keep this in mind for
# future projects.
# N.B - be very specific about your intentended outcome to the AI,
# it will help you get the best results. I did paste my own code in
# first so it was only trying to rewrite my awkward code, lol

from blackjack_fred_logo import logo
import random

import os

def clear():
    os.system('cls||clear')

def show_logo():
    print(logo)

# Define the card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Define the player class
class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []
        self.bet = 0

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

# Define the dealer class
class Dealer(Player):
    def show_hand(self, reveal=False):
        if reveal:
            return self.hand
        else:
            return [self.hand[0], 'X']

# Define the deck class
class Deck:
    def __init__(self, num_decks):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4 * num_decks
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Function to calculate the hand value
def calculate_hand_value(hand):
    value = sum([card_values[card] for card in hand])
    num_aces = hand.count('A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Function to check for blackjack
def check_blackjack(hand):
    return len(hand) == 2 and 'A' in hand and (hand.count('10') + hand.count('J') + hand.count('Q') + hand.count('K')) == 1

# Function to play a hand
def play_hand(player, dealer, deck):
    # Deal initial cards
    for _ in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

    # Check for player blackjack
    if check_blackjack(player.hand):
        player.money += int(player.bet * 1.5)
        result = 'Player has blackjack!'
    else:
        player_action = ""
        while player_action.lower() != 'stand' and calculate_hand_value(player.hand) < 21:
            player_action = input(f"{player.name}'s hand: {player.hand}, Dealer's card: {dealer.show_hand()[0]}\nHit or Stand? ")
            if player_action.lower() == 'hit':
                player.add_card(deck.deal_card())
            elif player_action.lower() == 'stand':
                break

        player_value = calculate_hand_value(player.hand)

        # Player bust
        if player_value > 21:
            player.money -= player.bet
            result = 'Player busts. Dealer wins.'
        else:
            # Dealer's turn
            while calculate_hand_value(dealer.hand) < 17:
                dealer.add_card(deck.deal_card())

            dealer_value = calculate_hand_value(dealer.hand)

            # Dealer bust
            if dealer_value > 21:
                player.money += player.bet
                result = 'Dealer busts. Player wins.'
            else:
                if player_value > dealer_value:
                    player.money += player.bet
                    result = 'Player wins!'
                elif player_value < dealer_value:
                    player.money -= player.bet
                    result = 'Dealer wins.'
                else:
                    result = 'Push - It\'s a tie.'

    player.clear_hand()
    dealer.clear_hand()

    return result

# Main function to run the game
def main():
    clear()
    show_logo()

    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        name = input(f"Enter player {i+1}'s name: ")
        money = int(input(f"Enter {name}'s starting money: "))
        players.append(Player(name, money))

    num_decks = int(input("Enter the number of decks to be used: "))
    num_hands = int(input("Enter the number of hands to be played: "))

    for _ in range(num_hands):
        deck = Deck(num_decks)
        dealer = Dealer("Dealer", float('inf'))
        for player in players:
            player.bet = int(input(f"{player.name}, enter your bet: "))
            print(play_hand(player, dealer, deck))

        print("\nPlayer results:")
        for player in players:
            print(f"{player.name}: {player.money}")

    winner = max(players, key=lambda x: x.money)
    print(f"\n{winner.name} is the overall winner with ${winner.money}!")

if __name__ == '__main__':
    main()
