# Higher lower game - guess the if the next answer popularity will be
# higher or lower than the previous one

from day_014_game_higher_lower_art import logo, vs
from day_014_game_higher_lower_data import data

import random
import os

# Function to clear the screen
def clear():
    os.system('cls||clear')

# Function to get a random account from the data
def get_random_account():
    random.choice(data)
    return

score = 0
game_over = False

while not game_over:
    # Clear screen and Display the logo
    clear()
    print(logo)
    # Get the first account
    account_a = get_random_account()
    print(f"{account_a}")
    # Get the second account
    account_b = get_random_account()
    print(f"{account_b}")


                                    # account_a == account_b:
                                    # account_b











# {
#     'name': 'Instagram',
#     'follower_count': 346,
#     'description': 'Social media platform',
#     'country': 'United States'
# },
