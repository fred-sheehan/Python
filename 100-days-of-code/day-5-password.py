#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

letters_choice = random.choices(letters, k=nr_letters)
numbers_choice = random.choices(numbers, k=nr_numbers)
symbols_choice = random.choices(symbols, k=nr_symbols)

password = letters_choice + numbers_choice + symbols_choice

random.shuffle(password)
print(f"Your password is: {''.join(password)}")

# Sample Output:
    # Welcome to the PyPassword Generator!
    # How many letters would you like in your password?
    # 8
    # How many symbols would you like?
    # 6
    # How many numbers would you like?
    # 4
    # Your password is: 8U%&Lj+%c+wF*5g2N2

# Now, I know we were supposed to use for loops to do this, but I wanted to try something different. I used the random.choices() method to randomly select the number of letters, numbers, and symbols the user wants in their password. I then concatenated the lists together and then shuffled them to create a random password. I used the join() method to convert the now random list to a string. I think this is a more efficient way to generate a password.

# more info on the random.choices() method here;
# https://www.geeksforgeeks.org/random-choices-method-in-python/

# but for completeness, here is the for loop version of the password generator, with just the logic, as we already have the lists above.

print("Welcome to the PyPassword Generator v2")
nr_letters= int(input("How many letters would you like in your password?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

# create a large list from our seperate lists
password_list = letters + numbers + symbols
# a holder for the items we pick
password2 = []

for _ in range(nr_letters):
    password2.append(random.choice(letters))

for _ in range(nr_numbers):
    password2.append(random.choice(numbers))

for _ in range(nr_symbols):
    password2.append(random.choice(symbols))

random.shuffle(password2)
print(f"Your password is: {''.join(password2)}")

# Sample Output:
    # Welcome to the PyPassword Generator v2
    # How many letters would you like in your password?
    # 8
    # How many symbols would you like?
    # 6
    # How many numbers would you like?
    # 4
    # Your password is: 2$QKIi57&!5Td2%t8k
