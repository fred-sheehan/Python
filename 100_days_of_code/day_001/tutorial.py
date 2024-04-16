# Hello World
print("\nHello World!\n")

# Auditorium challenge 1
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
print()

# Auditorium challenge 2
print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \\\"escape\\\" the quote\n")
print("Hello World!\nHello World!\nHello World!\n")
print("Hello" + " " + "Fred\n")

# Accepting input to be printed to the console
# Accepts the input first, then prints the expected output!
print("Hello " + input("What is your name? "))
firstName = input("\nWhat is your first name? ")
lastName = input("What is your last name? ")
namesLength = len(firstName) + len(lastName)
print("\nYour names together, contain " + str(namesLength) + " characters.\n")
