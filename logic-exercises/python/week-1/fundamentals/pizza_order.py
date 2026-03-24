PRICES = {"s": 15, "m": 20, "l": 25}
PEPPERONI_PRICES = {"s": 2, "m": 3, "l": 3}
EXTRA_CHEESE_PRICE = 1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: \n").lower()
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n").lower()
add_cheese = input("Do you want extra chesse? Y or N: \n").lower()

total_price = PRICES.get(size, 0)

if add_pepperoni == "y":
    total_price += PEPPERONI_PRICES.get(size, 0)

if add_cheese == "y":
    total_price += EXTRA_CHEESE_PRICE

if total_price > 0:
    print(f"Your final bill is: ${total_price}")
else:
    print("Invalid size selected. Please try again.")
