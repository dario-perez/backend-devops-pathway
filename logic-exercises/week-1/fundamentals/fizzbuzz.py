# FizzBuzz__________________________________________
for i in range(1, 101):
    word = ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
    print(word or i)
