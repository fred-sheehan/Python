import random
import os

from blackjack_logo import logo


def clear():
    os.system('cls||clear')


def show_logo():
    print(logo)


def exit_game():
    print("Thank you for playing, goodbye!")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_dealt):
    if sum(cards_dealt) == 21 and len(cards_dealt) == 2:  # Blackjack
        return 0

    hand_score = sum(cards_dealt)
    if 11 in cards_dealt and hand_score > 21:
        cards_dealt.remove(11)
        cards_dealt.append(1)
        # Recalculate hand score with the new ace value
        hand_score = sum(cards_dealt)

    return hand_score


def compare_scores(user_score, computer_score):
    if user_score == 0:
        print("Blackjack! You win!")
    elif computer_score == 0:
        print("Computer has Blackjack! Computer wins!")
    elif user_score > 21 and computer_score > 21:
        return "Both player and computer went over. It's a draw!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > 21:
        return "You went over. Computer wins!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"


def blackjack():
    clear()
    show_logo()
    print("Welcome to Blackjack!")
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    while user_score < 21:
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_choice == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
        else:
            break

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

    play_again = input(
        "Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'n':
        exit_game()
    else:
        blackjack()


blackjack()
