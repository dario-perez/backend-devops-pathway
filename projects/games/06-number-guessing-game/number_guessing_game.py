import random

logo = r'''
 _______               ___.                                                      .__                
 \      \  __ __  _____\_ |__   ___________     ____  __ __   ____   ______ _____|__| ____    ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \   / ___\|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/  / /_/  >  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >
\____|__  /____/|__|_|  /___  /\___  >__|     \___  /|____/  \___  >____  >____  >__|___|  /\___  / 
        \/            \/    \/     \/        /_____/             \/     \/     \/        \//_____/  
'''
new_game = True



print(logo)
print("=" * 50)
print("------ Welcome to the Number Guessing Game! ------")
print("=" * 50)
print("I'm thinking of a number between 1 and 100.")



while new_game:
    number = random.randint(1, 100)
    lives = 0
    players_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    won = False

    if players_choice not in ["easy", "hard"]:
        print("Wrong choice! Type 'easy' or 'hard': ")
        continue
    elif players_choice == "easy":
        lives = 10
    else:
        lives = 5

    print(f"You have {lives} attempts remaining to guess the number")

    while lives > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if number == guess:
            print(f"You win! The number was: {number}🔥")
            won = True
            break
        elif guess > number:
            print("Too high ⬆️")
        else:
            print("Too low ⬇️")

        lives -= 1

        if lives > 0:
            print("Guess again")
            print(f"---> You have {lives} attempts remaining to guess the number")

    if not won:
        print(f"You've run out of guesses, the number was: {number} You lose ❌\n")

    while True:
        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play_again in ["y", "n"]:
            break
        print("Please type 'y' or 'n'")

    if play_again == "y":
        print("\n" * 50)
        continue
    else:
        print("Thank you for playing!")
        new_game = False