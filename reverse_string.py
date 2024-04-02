# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Taking input from the user
input_string = input("Enter a to reverse: ")

# Reversing the string
reversed_string = reverse_string(input_string)

# Displaying the reversed string
print("Reversed string:", reversed_string)
