# Function to reverse a string

    # reversing a string using slicing - fastest/best way
def reverse_string(input_string):
    return input_string[::-1]

    # taking string from variable
input_string = "Hello, World!"

    # Taking input from the user
input_string = input("Enter a string to reverse: ")

    # Reversing the string using the function
reversed_string = reverse_string(input_string)

    # Displaying the reversed string
print("Reversed string:", reversed_string)
