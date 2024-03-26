# Data Types

# Strings
# Subscripting in Python
print("Hello"[0]) # H
print("Hello"[1]) # e
print("Hello"[2]) # l
print("Hello"[3]) # l
print("Hello"[4]) # o
print()

# Integers
print(123 + 345) # 468
# can use underscores to make it more readable
print(123_456_789) # 123456789

# Float
print(3.14159) # 3.14159
print(1_000 * 3.14159)
print()

# Boolean
print(True) # True
print(False) # False

# Auditorium challenge
# next line added to get user input for local use
print("\nEnter any 2 digit number: ")
# 🚨 Don't change the code below 👇
two_digit_number = input()
####################################
# Write your code below this line 👇
digit_1 = int(two_digit_number[0])
digit_2 = int(two_digit_number[1])
print(digit_1 + digit_2)

# Mathematical operations
# Addition
print(3 + 5) # 8
# Subtraction
print(7 - 4) # 3
# Multiplication
print(3 * 2) # 6
# Division
print(6 / 3) # 2.0
# Exponentiation - (power)
print(2 ** 3) # 8
# Floor division - (integer division, ignores the decimal part)
print(121 // 4) # 30
# Modulo - (only gives remainder)
print(7 % 4) # 3

# PEMDASLR or BODMASLR (Brackets(), Orders **, Division and Multiplication / * or * /, Addition and Subtraction + - or - +, Left-to-right decides tie))
print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0

# BMI Calculator
# 1st input: enter height in meters e.g: 1.65
# next line added to get user input for local use
print("\nEnter your height in meters: ")
height = input()
# 2nd input: enter weight in kilograms e.g: 72
# next line added to get user input for local use
print("\nEnter your weight in kilograms: ")
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
height_as_float = float(height)
weight_as_float = float(weight)
bmi_as_integer = int(weight_as_float / (height_as_float * height_as_float))
# could have also used,  height_as_float ** 2
print("Your BMI score is: " + str(bmi_as_integer))
print()

# Using Pythons round() function
print(round(8 / 3)) # 3
# Or we can specify how many decimal places to use
print(round(8 / 3, 2)) # 2.67
print(round(8/3, 4)) # 2.6667

# Floor division - this will always give an integer
# reduced to the lowest whole number (the floor)
print(8 // 3) # 2

# F-String
# f-string is an easier way to format strings in Python
score = 125
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, are you winning? {isWinning}")

# Life in weeks challenge
# next line added to get user input for local use
print("\nWhat is your current age? ")
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
average_lifespan_in_weeks = 90 * 52
your_used_weeks = int(age) * 52
weeks_left = average_lifespan_in_weeks - your_used_weeks
print(f"You have {weeks_left} weeks left.")

# Day 2 Project: Tip Calculator
# Greeting
print("\nWelcome to the tip calculator.\n")
# 1st input: enter total bill amount
print("What was the total bill?" + input())
total_bill = float(input())
# 2nd input: enter percentage tip to give
print("What percentage tip would you like to give? 10, 12, or 15 ?" + input())
tip_percentage = int(input())
# 3rd input: enter number of people to split the bill
print("How many people to split the bill between?" + input())
number_of_people = int(input())
# Calculate the tip
tip = total_bill * (tip_percentage / 100)
# Calculate the total bill with tip
total_bill_with_tip = total_bill + tip
# Calculate the bill per person
bill_per_person = total_bill_with_tip / number_of_people
# Round the bill per person to 2 decimal places
final_amount = round(bill_per_person, 2)
# Display the final amount
print(f"Including the tip, each person should pay ${final_amount}")

# version 2 - much more terse!
print("\nWelcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = round(bill_with_tip / people, 2)
# the following line ensures we always have 2 decimal places in our output format, even if theya re both 0
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")
