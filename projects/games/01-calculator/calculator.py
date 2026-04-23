import os



logo = '''
   _____________________
  |  _________________  |
  | | JO           0. | |
  | |_________________| |
  |  ___ ___ ___   ___  |
  | | 7 | 8 | 9 | | + | |
  | |___|___|___| |___| |
  | | 4 | 5 | 6 | | - | |
  | |___|___|___| |___| |
  | | 1 | 2 | 3 | | x | |
  | |___|___|___| |___| |
  | | . | 0 | = | | / | |
  | |___|___|___| |___| |
  |_____________________|

'''

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  if n2 == 0:
     return 0
  return n1 / n2



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

print("======== CALCULATOR ========")
print(logo)

while True:
  number_1 = float(input("What's the first number? "))

  while True:
    for symbol in operations:
      print(symbol)
    operation_option = input("Pick an operation: ")
    number_2 = float(input("What's the next number? "))

    operation = operations[operation_option]
    result = operation(number_1, number_2)
    print(f"{number_1} {operation_option} {number_2} = {result:.1f}")

    continue_option = input(
      f"Type 'y' to continue calculating with {result:.1f} or type 'n' to start a new calculation: "
    )

    if continue_option.lower() == "y":
      number_1 = result
      continue
    else:
      clear()
      break