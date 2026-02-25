# Heads and tails_______________________________________________________
# import random


# def flip_a_coin():
#     return "Heads" if random.randint(0, 1) == 1 else "Tails"


# print(flip_a_coin())


# Who pays the bill_______________________________________________________
# import random

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# # option1 (with index)
# print(f"who pays the bill is: {friends[random.randrange(len(friends))]}!")
# # option2 (without index)
# print(f"Who pays the bill is: {random.choice(friends)}")


# Rock, paper, scissors_______________________________________________________
# nums = [
#     142,
#     27,
#     89,
#     115,
#     12,
#     56,
#     134,
#     43,
#     98,
#     71,
#     29,
#     108,
#     41,
#     74,
#     125,
#     17,
#     79,
#     113,
#     58,
# ]

# max_num = 0

# for num in nums:
#     if num > max_num:
#         max_num = num

# print(max_num)


# Password generator_______________________________________________________
# import random

# LETTERS = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
#     "A",
#     "B",
#     "C",
#     "D",
#     "E",
#     "F",
#     "G",
#     "H",
#     "I",
#     "J",
#     "K",
#     "L",
#     "M",
#     "N",
#     "O",
#     "P",
#     "Q",
#     "R",
#     "S",
#     "T",
#     "U",
#     "V",
#     "W",
#     "X",
#     "Y",
#     "Z",
# ]

# NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# SYMBOLS = ["#", "$", "%", "&", "@", "!", "?", "*", "+"]

# password = []

# print("welcome to the PyPassword Generator!")
# n_letters = int(input("How many letters would you like?\n"))
# n_numbers = int(input("How many numbers would you like?\n"))
# n_symbols = int(input("How many symbols would you like?\n"))

# password.append(random.choices(LETTERS, k=n_letters))
# password.append(random.choices(NUMBERS, k=n_numbers))
# password.append(random.choices(SYMBOLS, k=n_symbols))

# flat_password = password[0] + password[1] + password[2]
# random.shuffle(flat_password)

# print(f"{''.join(flat_password)}")
