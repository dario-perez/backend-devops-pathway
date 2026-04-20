from data import MENU, RESOURCES
from art import logo_display



# --------------> VARIABLES <--------------
turn_on = True
money = 0
allowed_prompts = [
    "report", 
    "menu", 
    "off", 
    "espresso", 
    "latte", 
    "cappuccino",
]



# --------------> FUNCTIONS <--------------
def format_resources(data):
    '''Formats RESOURCES to printable data'''
    return(    
        f"Water: {data['water']}ml\n"
        f"Milk: {data['milk']}ml\n"
        f"Coffee: {data['coffee']}g\n"
    )

def report():
    '''Prints a report of the resources available + money available in the machine'''
    global money
    print("\n====== REMAINING INGREDIENTS ======")
    print(format_resources(RESOURCES))
    print(f"Money: ${money:.2f}\n")

def show_menu():
    '''Shows the items available in the MENU'''
    print("\n====== MENU ======")
    for item in MENU:
        cost = MENU[item]["cost"]
        print(f"{item.capitalize():12} - ${cost:.2f}")

def process_coins():
    '''Asks user for coins and returns total money inserted'''
    print("Please insert coins:")
    quarters = int(input("How many quarters?: ($0.25): "))
    dimes = int(input("How many dimes?: ($0.10): "))
    nickels = int(input("How many nickels?: ($0.05): "))
    pennies = int(input("How many pennies?: ($0.01): "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total

def sufficient_resources(choice):
    '''Checks if there are enough ingredients left'''
    for ingredient, required in MENU[choice]["ingredients"].items():
        if RESOURCES[ingredient] < required:
            print(f"Not enough {ingredient}")
            return False
    return True

def make_coffee(choice):
    '''Deducts ingredients and serves the coffee'''
    global money

    for ingredient, required in MENU[choice]["ingredients"].items():
        RESOURCES[ingredient] -= required

    money += MENU[choice]["cost"]
    print(f"Here is your {choice.capitalize()} ☕ Enjoy!")

def turn_off():
    '''Turns off the machine'''
    global turn_on
    turn_on = False
    print("Machine is turning off... Goodbye!")



# --------------> RUN PROGRAM <--------------
logo_display()

while turn_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        report()

    elif choice == "menu":
        show_menu()

    elif choice == "off":
        turn_off()

    elif choice in ["espresso", "latte", "cappuccino"]:
        if sufficient_resources(choice):
            money_inserted = process_coins()
            cost = MENU[choice]["cost"]

            if money_inserted >= cost:
                change = money_inserted - cost
                print(f"Here is ${change:.2f} in change")
                make_coffee(choice)
            else:
                print(f"Sorry, that's not enough money. ${money_inserted:.2f} inserted, ")
                print("Money refunded")
    else:
        print("Invalid input. Please choose from: \nespresso, \nlatte, \ncappuccino, \nreport, \nmenu, \noff")

print("Machine is now off")