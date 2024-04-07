#Password Generator Project using for loops
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# first version of the password generator - Easy
print("Welcome to the PyPassword Generator")
nr_letters= int(input("How many letters would you like in your password?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

# we create an empty string to store the generated password
password = ''

for char in range(1, nr_letters +1):
    password += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(f"Your password is: {password}")

# Sample Output:
    # Welcome to the PyPassword Generator v2
    # How many letters would you like in your password?
    # 6
    # How many symbols would you like?
    # 5
    # How many numbers would you like?
    # 4
    # Your password is: VBWPWt61306*%)+

# version 2 with shuffling of generated password - Hard
print("Welcome to the PyPassword Generator v2")
nr_letters= int(input("How many letters would you like in your password?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

# we create an empty list to store the generated password
password_list = []

for char in range(1, nr_letters +1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

print(f"Your password is: {password}")

# now we shuffle the list (you cant do this on a string)
random.shuffle(password_list)

# and then create an empty string as earlier
password = ''

# now we loop through the list and add each character to the password string
for char in password_list:
    password += char
print(f"Your shuffled password is: {password}")

# Sample Output:
    # Welcome to the PyPassword Generator!
    # How many letters would you like in your password?
    # 6
    # How many symbols would you like?
    # 5
    # How many numbers would you like?
    # 4
    # Your password is: A1Fl4p&!+P!x038
