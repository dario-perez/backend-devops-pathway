from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



if __name__ == "__main__":
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True

    print("\n======= Menu: =======")
    print(menu.get_items())
    while is_on:
        option = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        if option == "off":
            is_on = False
            print("Machine is turning off... Goodbye!")
        elif option == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(option)
            if drink is None:
                print("Sorry that item is not available.")
                continue

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)