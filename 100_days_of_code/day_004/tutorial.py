# random numbers
# import the python random module
import random

# generate a random number between 0 and 20
random_integer = random.randint(0, 20)
print(random_integer)

# generate a random number between 0 and 1
random_float = random.random()
print(random_float)
# so if we want to generate a random number between 0 and 5
print(random_float * 5)

# love calculator no 2
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


# Heads or Tails
# import random

random_coin_side = random.randint(0, 1)
if random_coin_side == 1:
  print("Heads")
else:
  print("Tails")


# Lists
# Lists are a data structure in Python that can store multiple values.
# They are ordered, changeable, and allow duplicate values.
# Lists are defined by square brackets [] and can be accessed by index.
# Lists can contain any data type, including other lists.

fruits = ["Apple", "Banana", "Cherry", 256, 32, "Tomato"]

american_states_today = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
    "Connecticut", "Massachusetts", "Maryland", "South Carolina",
    "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
    "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
    "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
    "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
    "Hawaii"]

american_states_original = ["Virginia", "South Carolina", "New York",
    "Rhode Island", "Connecticut", "Georgia", "New Hampshire", "Pennsylvania",
    "Massachusetts", "North Carolina", "New Jersey", "Delaware", "Maryland"]

# List Indexing can be from beginning, positive index, or from the end, negative index.
american_states_today[0] # Delaware
american_states_today[-1] # Hawaii

# add an item to the end of the list
american_states_original.append("Vermont")
# add an item to the beginning of the list
american_states_original.insert(0, "Kentucky")

# remove the last item from the list
american_states_original.pop()
# remove the first item from the list
american_states_original.pop(0)


# Banker roulette
# below line commented out for local testing, uncomment for auditorium tests
# names = names_string.split(", ")

# import  random
# below line added for local testing, comment out for auditorium tests
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random_payer = random.randint(0, len(names) - 1)

print(f"{names[random_payer]} is going to buy the meal today!")


# Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches",
    "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


# Treasure Map
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
# code changed below for local use
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

if  position == 'A1':
  line1[0] = 'X'
if  position ==  'A2':
  line2[0] = 'X'
if  position == 'A3':
  line3[0] = 'X'

if  position == 'B1':
  line1[1] = 'X'
if  position == 'B2':
  line2[1] = 'X'
if  position == 'B3':
  line3[1] = 'X'

if  position == 'C1':
  line1[2] = 'X'
if  position == 'C2':
  line2[2] = 'X'
if  position == 'C3':
  line3[2] ='X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

# my (poor) code example above worked, and passed all tests, but the code below
# is far more efficient (and elegant)

# Treasure Map 2
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
