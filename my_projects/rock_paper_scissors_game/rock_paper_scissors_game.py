# Rock, Paper, Scissors game with Ascii Art
# We will need random module to generate computer choice
import random

# Ascii art for Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Game and game logic start below
print("Welcome to Rock, Paper, Scissors!")

# User choice logic
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

# Computer choice logic
computer_choice = random.randint(0, 2)
print(f"Computer chose:")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

# Who wins?
# If user doesn't win, computer does, so we only need to check for user wins!
if user_choice == computer_choice:
    print("Draw!")
elif user_choice == 0 and computer_choice == 2:
    # Rock beats Scissors
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    # Paper beats Rock
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    # Scissors beats Paper
    print("You win!")
else:
    # else computer wins
    print("You lose!")
