import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

print("Type in a word and have the NATO phonetic alphabet equivalent displayed.")

while True:
    user_word = input("Enter a word: ").upper()
    try:
        output_word_list = [nato_phonetic_alphabet[letter] for letter in user_word]
        break
    except KeyError:
        print("Letters only please.")

print(output_word_list)
