# Ascii art Hangman in Python

from day_007_hangman_word_list import word_list
import gallows_stages
import random

def new_game():
    print("Welcome to Hangman!")

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6
    guessed_letters = []

    display = []
    for _ in range(word_length):
        display.append("_")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        display_output = " ".join(display)
        print(display_output)

        if "_" not in display:
            end_of_game = True
            print("You win")

        elif guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

        guessed_letters.append(guess)
        print(f"Already guessed: {guessed_letters}")
        print(f"Lives remaining: {lives}")

        if lives == 0:
            end_of_game = True
            print("You lose.")

        print(gallows_stages[lives])

another_game = input("\n Would you like another game of Hangman? y/n ").lower()
if another_game == "y":
    new_game()
else:
    print("Goodbye! Thanks for playing!")
