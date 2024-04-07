# Coffee Machine Project

# imports
from coffee_machine_project_menu import MENU, resources
import time
import os

# import initial machine start up resources levels data
resources = resources.copy()

# clear screen function
def clear():
    os.system('cls||clear')

# print machine current resources levels
def print_report():
    print(
        f"Current Machine Resources:\nWater: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g\nMoney: $ {resources['money']}"
    )

# check if current machine resources are sufficient
# to fulfill customers order
def check_resources(order):
    for item in MENU[order]['ingredients']:
        if resources[item] < MENU[order]['ingredients'][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            return True

# check if customer has inserted enough money for order
def check_transaction(order, money):
    cost = MENU[order]['cost']
    print(f"Cost of {order} is ${cost}.")
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change.")
        time.sleep(2)
        return
    else:
        print("Sorry that's not enough money. Money refunded.")
        time.sleep(2)
    coffee_machine()

# if order was successful, update current machine resources
def update_resources(order):
    for item in MENU[order]['ingredients']:
        resources[item] -= MENU[order]['ingredients'][item]
        resources['money'] += MENU[order]['cost']

def process_order(order):
    if order == 'report':
        print_report()
    elif order == 'off':
        print("Shutting down the Coffee Machine.")
        time.sleep(2)
        exit()
    elif order == 'cappuccino' or order == 'latte' or order == 'espresso':
        if check_resources(order):
            print("Please insert coins.")
            money = float(input("How many quarters?: ")) * 0.25
            money += float(input("How many dimes?: ")) * 0.10
            money += float(input("How many nickels?: ")) * 0.05
            money += float(input("How many pennies?: ")) * 0.01
            check_transaction(order, money)
            print(f"Here is your {order}. Enjoy!")
            update_resources(order)

# main function
def coffee_machine():
    clear()
    print("Welcome to the Coffee Machine!")
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        process_order(order)

# run the coffee machine
coffee_machine()
