# Initial def
a = "Red Liquid"
b = "Blue Liquid"

print(f"Before: A={a}, B={b}")

# Solution: Using a temp variable
temp = a
a = b
b = temp

print(f"After: A={a}, B={b}")
