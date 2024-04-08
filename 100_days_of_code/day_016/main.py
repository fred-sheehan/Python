from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
        print("Turning Coffee Machine Off")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if order:
            order = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)
