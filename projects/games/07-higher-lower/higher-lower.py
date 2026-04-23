import random
from data import data

logo = r'''
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                         
                                                                         
░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█████████████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                         
'''

vs = r'''
░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░ ░▒▓██████▓▒░  
  ░▒▓█▓▓█▓▒░        ░▒▓█▓▒░ 
  ░▒▓█▓▓█▓▒░        ░▒▓█▓▒░ 
   ░▒▓██▓▒░  ░▒▓███████▓▒░  
                            
'''

# PRINT LOGO
print(logo)

# SEARCH FOR THE FIRTS RANDOM CELEBRITY
### GET CELEBRITY DATA
def random_index():
    return random.randrange(len(data))

celeb_a = random_index()
score = 0

while True:
    celeb_b = random_index()

    while celeb_b == celeb_a:
        celeb_b = random_index()

    print(f"Compare A: {data[celeb_a]['name']}, {data[celeb_a]['description'].capitalize()}, from: {data[celeb_a]['country']}\n")

    # PRINT VS
    print(vs)

    # SEARCH FOR THE SECOND RANDOM CELEBRITY
    ### GET CELEBRITY DATA
    print(f"Against B: {data[celeb_b]['name']}, {data[celeb_b]['description'].capitalize()}, from: {data[celeb_b]['country']}\n")

    # CHECK WHICH OF BOTH FOLLOWERS NUMBERS ARE GREATER THAN THE OTHER ONE
    followers_a = data[celeb_a]["followers_acount"]
    followers_b = data[celeb_b]["followers_acount"]
    players_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if players_choice not in ["a", "b"]:
        print("Invalid input")
        continue

    if followers_a > followers_b:
        correct_answer = 'a'
    else:
        correct_answer = 'b'

    # IF THE CHOOSEN NUMBER IS GREATER, CONTINUE TO THE NEXT COMPARISON. OTHERWISE, GAME OVER
    if players_choice == correct_answer:
        score += 1
        celeb_a = celeb_b
        print("\n" * 20)
        print(f"You're right! Current score: {score}")
        continue
    else:
        print(f"Sorry, that's wrong! Final score: {score}")
        break