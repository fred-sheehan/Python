#For Loop, were going to replace this method with..
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list) # [2, 3, 4]

# .... list comprehension!
# new_list = [new_item for item in list]
# for example
new_numbers = [x + 1 for x in numbers]
print(new_numbers) # [2, 3, 4]
more_numbers = [item + 10 for item in numbers]
print(more_numbers) # [11, 12, 13]

# list comprehension with string
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list) # ['A', 'n', 'g', 'e', 'l', 'a']

# list comprehension with range
# new_list = [new_item for item in range]
# for example
squared_numbers = [x * x for x in range(1, 5)]
print(squared_numbers) # [1, 4, 9, 16]
doubled_numbers = [x * 2 for x in range(1, 5)]
print(doubled_numbers) # [2, 4, 6, 8]

# list comprehension with condition
# new_list = [new_item for item in list if test]
# for example
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(names) # ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 5]
print(short_names) # ['Alex', 'Beth', 'Dave']
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names) # ['CAROLINE', 'ELEANOR', 'FREDDIE']

# create list of even numbers from a list of strings
# following list added for offline use
nums_as_strings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
print(nums_as_strings)
# first split them into individual strings using split method
# not used here, auditorium code from angela
## list_of_strings = input().split(',')
# instead i'll copy my previously added list
list_of_strings = nums_as_strings

# Use list comprehension to convert the strings to integers
# and store the integers in a list called "list_of_numbers"
list_of_numbers = [int(x) for x in list_of_strings]
print(list_of_numbers)

# Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [num for num in list_of_numbers if num%2 == 0]
print(result)

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

# convert the strings to integers and check the common numbers
result = [int(num) for num in list1 if num in list2]
print(result)

# dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(names)

import random
# new_dictionary = {new_key:new_value for item in list}
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# new_dictionary = {new_key:new_value for (key, value) in dictionary.items()}

# new_dict = {new_key:new_value for (key, value) in dictionary.items() if test}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# create dictionary from input, split to words with character count
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# new_dictionary = {new_key:new_value for new_key in dictionary}
result = {word:len(word) for word in sentence.split()}
print(result)

# create new dictionary from weather_c dictionary converted to temperature in F
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
print(weather_c)
# To convert temp_c into temp_f use this formula:
#(temp_c * 9/5) + 32 = temp_f

# new_dictionary = {new_key:new_value for (key, value) in dictionary.items()}
weather_f = {day:temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# looping through dictionaries - create a dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# looping through the dictionary
for (key, value) in student_dict.items():
    print(value)

# now using pandas, first create a pandas data frame
import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# then loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
