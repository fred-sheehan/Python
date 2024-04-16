# Higher lower game
import random
import time
import os

from higher_lower_game_art import logo, vs
from higher_lower_game_data import data


def clear():
    os.system('cls||clear')


def get_random_account():
    account = random.choice(data)
    return account


def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"


#checks which account has more followers
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    game_over = False
    account_a = get_random_account()
    account_b = get_random_account()

    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        # if the random accounts are the same, get another account
        while account_a == account_b:
            account_b = get_random_account()

        clear()
        print(f"Current score: {score}")
        print(logo)
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        user_choice = input(
            "\nWho has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(
            user_choice, a_follower_count, b_follower_count
        )
        if is_correct:
            score += 1
            print(f"\nYou're right! Current score: {score}.")
            time.sleep(1.5)
        else:
            game_over = True
            print(f"\nSorry, that's wrong. Final score: {score}")

    new_game = input(
        "\nDo you want to play again? Type 'yes' or 'no': ").lower()
    if new_game == "yes" or new_game == "y":
        game()
    else:
        print("Thank you for playing. Goodbye!")


game()
