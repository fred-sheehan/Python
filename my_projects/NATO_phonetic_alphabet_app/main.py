import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)

nato_phonetic_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()

output_word_list = [nato_phonetic_alphabet[letter] for letter in user_word]

print(output_word_list)
