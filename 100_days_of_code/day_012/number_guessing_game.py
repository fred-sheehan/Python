# simple number guessing game
import random
import os


def clear():
    os.system('cls||clear')


def guess_number():
    play_again = True
    random_number = random.randint(1, 101)
    clear()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        number_of_attempts = 5
    else:
        number_of_attempts = 10

    while play_again:
        if number_of_attempts > 0:
            print(f"You have {number_of_attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))

            if guess == random_number:
                print(f"You guessed the right number: {random_number}")
                play_again = False

            elif guess < random_number:
                    print("Too low.")
                    number_of_attempts -= 1
            else:
                print("Too high.")
                number_of_attempts -= 1

        if number_of_attempts == 0:
            play_again = False
            print(f"You've run out of guesses. The correct number was {random_number}")

    new_game = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if new_game == "y":
        guess_number()
    else:
        print("Goodbye!")

guess_number()
