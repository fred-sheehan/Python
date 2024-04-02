def greet(name):
    print(f"Hello {name}")
    print(f"Good Morning {name}")
    print(f"Good Night {name}")

greet(name = input("Enter your name: "))


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}")

greet_with(name = (input("What is your name? ")), location = (input("Where are you from? ")))


def prime_checker(number):
    is_prime = True

    if number == 1:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

prime_checker(number = int(input("Enter a number: ")))
