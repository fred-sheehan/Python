# Higher lower game - guess the if the next answer popularity will be
# higher or lower than the previous one

# import the game logos and data from the other files
from day_014_game_higher_lower_art import logo, vs
from day_014_game_higher_lower_data import data

# import random module to pick random account from data, os module to
# create clear the screen function, and time to create delays in code
import random
import time
import os

# Function to clear the screen
def clear():
    # Windows it will use 'cls' to clear the screen, for linux/unix/Mac OSX
    # will use 'clear' (outputs 'cls' or 'clear' directly to the terminal)
    os.system('cls||clear')

# Function to get a random account from the data
def get_random_account():
    account = random.choice(data)
    return account

# Function to format the data to easily call it already formatted for use
# in the game, and without the follower count to be displayed
def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

# function that checks which account has more followers
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# game function
def game():
    # set up game start
    score = 0
    game_over = False
    account_a = get_random_account()
    account_b = get_random_account()

    # while the game is not over
    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        # if the random accounts are the same, get another account
        while account_a == account_b:
            account_b = get_random_account()

        # clear the screen and print the first game logo
        clear()
        print(f"Current score: {score}")
        print(logo)
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        user_choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        # get the follower count of each account
        # and check if the user's guess is correct
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(user_choice, a_follower_count, b_follower_count)
        if is_correct:
            score += 1
            print(f"\nYou're right! Current score: {score}.")
            time.sleep(1.5)
        else:
            game_over = True
            print(f"\nSorry, that's wrong. Final score: {score}")

    new_game = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
    if new_game == "yes" or new_game == "y":
        game()
    else:
        print("Thank you for playing. Goodbye!")

# start the game
game()
