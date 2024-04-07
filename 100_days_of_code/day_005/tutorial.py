# loops in Python

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit +  " is a fruit")


# for loop to find average heights
# Input a list of student heights
student_heights = [132, 145, 176, 150, 140]
# ========================================

total_height = 0
num_of_students = 0

for height in student_heights:
    total_height += height
    num_of_students +=1

average_height = round(total_height / num_of_students)

print(f"total height = {total_height}")
print(f"number of students = {num_of_students}")
print(f"average height = {average_height}")


# calculate heighest score in a list
# Input a list of student scores
student_scores = [81, 73, 62, 95, 72, 78]
# ========================================

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")


# for loop with range
# range(start, stop, step) note, stop is not inclusive!
for number in range(1, 10): # 1 to 9
    print(number)

for number in range(1, 10, 2): # 1 to 9, step 2
    print(number)


# sum of all even numbers from 1 to user input
target_num = int(input("What maximum number would you like to add up the even numbers for? "))

evens_sum = 0
for number in range(1, target_num + 1):
    if number % 2 == 0:
        evens_sum += number

print(evens_sum)

# another way to do the same thing
# dont forget to reset even_sum to 0
evens_sum = 0
# if we want to use the range() step function, for even numbers we have to start with 2 else we would the sum odd numbers in increments of 2!
for number in range(2, target_num + 1, 2):
        evens_sum += number

print(evens_sum)


# fizzbuzz
# if number is divisible by 3, print "Fizz"
# if number is divisible by 5, print "Buzz"
# if number is divisible by 3 and 5, print "FizzBuzz"
# else print the number

# ask user for a target number to run fizzbuzz to
target_num = int(input("What maximum number would you like to run FizzBuzz to? "))

for number in range(1, target_num + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
