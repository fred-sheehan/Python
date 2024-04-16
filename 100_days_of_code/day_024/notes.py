# Python read from a file
with open("/Users/fred/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

# Python write to a file - note the need of 'mode' parameter
# iof file doesn't exist, it will be created!
with open("/Users/fred/Desktop/new_file.txt", mode="w") as file:
    file.write("\nAdd some text, play around, but do take care, is your judgment sound?")
    print(file)

# Python append to a file instead of overwriting it!
with open("my_file.txt", mode="a") as file:
    file.write("\n\nThat's much better, we kept our text, don't wipe it out, that's never best!")
    print(file)
