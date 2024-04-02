# Conditional Logic

# A rollercoaster min height requirement of 120cm or above
print("Welcome to the Rollercoaster.")
height = int(input("How tall are you in cm? "))
if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you have to grow taller before you can ride the Rollercoaster.")


# Odd or Even
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


# Rollercoaster part 2
print("Welcome to the Rollercoaster part 2.")
height = int(input("How tall are you in cm? "))
if height >= 120:
    age = int(input("Please enter your age: "))
    if age <= 12:
        print("Please pay $5.")
    elif age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride the Rollercoaster.")


# BMI Calculator v.2
print("Welcome to the BMI Calculator 2.0")
height = float(input("Please enter your height in Metres (e.g. 1.75): "))
weight = int(input("Please enter your weight to the nearest Kg (e.g. 75): "))
bmi = weight / (height * height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


# Leap Year calculator
print("Welcome to the Leap Year Calculator.")
year = int(input("Please enter a year (e.g., 2021): "))
# Is year divisible by 4?
if year % 4 == 0:
    # If year is divisible by 4, is it divisible by 100?
    if year % 100 == 0:
        # If year is divisible by 100, is it divisible by 400?
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")


# Rollercoaster part 3
print("Welcome to the Rollercoaster part 3.")
height = int(input("How tall are you in cm? "))
if height >= 120:
    cost = 0
    age = int(input("Please enter your age: "))
    if age <= 12:
        cost += 5
        print(f"Child tickets cost ${cost}")
    elif age < 18:
        cost += 7
        print(f"Teen tickets cost ${cost}")
    else:
        cost += 12
        print(f"Adult tickets cost ${cost}")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y":
        cost += 3
    print(f"Your total cost is ${cost}.")
else:
    print("Sorry, you have to grow taller before you can ride the Rollercoaster. :(")


# Pizza Order
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? (S, M, or L) ")
add_pepperoni = input("Do you want pepperoni? (Y or N) ")
extra_cheese = input("Do you want extra cheese? (Y or N) ")

cost = 0

if size == "S":
  cost += 15
elif size == "M":
  cost += 20
else:
  cost += 25

if add_pepperoni == "Y":
  if size == "S":
    cost += 2
  else:
    cost +=3

if extra_cheese == "Y":
  cost += 1

print(f"Your final bill is: ${cost}")


# Rollercoaster part 4
print("Welcome to the Rollercoaster part 4.")
height = int(input("How tall are you in cm? "))
if height >= 120:
    cost = 0
    age = int(input("Please enter your age: "))

    if age <= 12:
        cost += 5
        print(f"Child tickets cost ${cost}")
    elif age < 18:
        cost += 7
        print(f"Teen tickets cost ${cost}")
    else:
        if age >= 45 and age <= 55:
            cost += 0
            print(f"Adult Mid-life crisis tickets cost ${cost}")
        else:
            cost += 12
            print(f"Adult tickets cost ${cost}")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y":
        cost += 3
    print(f"Your total cost is ${cost}.")
else:
    print("Sorry, you have to grow taller before you can ride the Rollercoaster. :(")


# 💕 Love Calculator 💕
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

digit1 = t + r + u + e
digit2 = l + o + v + e

score = str(digit1) + str(digit2)

if int(score) < 10 or int(score) > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif  int(score) >= 40 and int(score) <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
