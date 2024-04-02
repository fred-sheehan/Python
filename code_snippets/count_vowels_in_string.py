# You can run this program and enter a string as input. The program will then count and display the number of vowels in the input string.

def count_vowels(string):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in string:
        if char.lower() in vowels:
            vowel_count += 1
    
    return vowel_count

input_string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_string))