# list comprehension
# new_list = [new_item for item in list]
# for example
numbers = [1, 2, 3]
print(numbers) # [1, 2, 3]
new_numbers = [x + 1 for x in numbers]
print(new_numbers) # [2, 3, 4]
more_numbers = [item +10 for item in numbers]
print(more_numbers) # [11, 12, 13]

# list comprehension with string
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list) # ['A', 'n', 'g', 'e', 'l', 'a']

# list comprehension with range
# new_list = [new_item for item in range]
# for example
squared_numbers = [x*x for x in range(1, 5)]
print(squared_numbers) # [1, 4, 9, 16]
doubled_numbers = [x*2 for x in range(1, 5)]
print(doubled_numbers) # [2, 4, 6, 8]

# list comprehension with condition
# new_list = [new_item for item in list if test]
# for example
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(names) # ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
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

# Use list comprehension to filter out the odd numbers (modulo)
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
