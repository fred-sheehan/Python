# Calculator
from calculator_logo import logo
import os

def clear():
    os.system('cls||clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def end_now():
    print("Thank you for trying the calculator. Goodbye!")

clear()

def calculator():
    print(logo)

    num1 = float(input("+"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        decide = input(f"Type 'y' to continue with {answer}, 'n' to start a new calculation, or 'e' to exit: ")
        if decide == 'y':
            num1 = answer
        elif decide == 'n':
            should_continue = False
            clear()
            calculator()
        else:
            should_continue = False
            end_now()

calculator()
