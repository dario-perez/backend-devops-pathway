# age = int(input("Write your age, please: "))

# if age >= 19:
#     print("Welcome to the Club. Come in!")
# elif age == 18:
#     print("Come back next year for your membership")
# else:
#     print("You are underage. You are not allowed to enter.")


age = int(input("Write your age, please: "))

if age >= 65:
    print("Free ticket")
elif age >= 13 and age <= 18:
    print("Student Discount")
else:
    print("Normal Fee")
