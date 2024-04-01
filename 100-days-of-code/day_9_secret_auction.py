# Blind bid auction program
import os
from gavel_logo import logo

def clear():
    os.system('cls||clear')

clear()
print(logo)

input("Welcome to the secret auction program.")

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == 'no':
        break
    clear()
