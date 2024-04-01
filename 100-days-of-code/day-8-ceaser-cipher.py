# Ceaser Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import os
from ceaser_cipher_logo import logo

os.system('cls||clear')
print(logo)

def ceaser(start_text, shift_amount, cipher_direction):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        else:
            output_text += char
    print(f"The {cipher_direction}d text is: {output_text}")

use_cipher = True

while use_cipher:
    user_decision = input("Do you want to use the Ceaser Cipher? yes/no:\n").lower()

    if user_decision not in ["no", "yes"]:
        print("Invalid input, please try again.")
        continue

    elif user_decision == "no":
        use_cipher = False
        print("Thank you for trying the ceaser cipher, goodbye!")

    elif user_decision == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction not in ["encode", "decode"]:
            print("Invalid input, please try again.")
            continue

        text = input("Type your message:\n").lower()

        try:
            shift = int(input("Type the shift number:\n"))
        except:
            print("Invalid input, please try again.")
            continue
        shift = shift % 26

        ceaser(cipher_direction = direction, start_text = text, shift_amount = shift)
