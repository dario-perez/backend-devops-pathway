import random

logo = '''
=========== BLACKJACK ===========
⠀⠀⠀⠀⠀⠀⣀⣤⣴⣄⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣿⣿⠛⠿⣿⣿⣿⡀⢻⣿⣿⣿⣿⠀⣸⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣿⣿⠃⠀⠀⠀⠈⠙⣧⠈⢿⣿⣿⣿⠀⣿⣿⣿⣿⡟⢀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⡇⠀⠀⠀⠀⣀⣠⣿⣇⠘⣿⣿⣿⠀⣿⣿⣿⡿⠀⣾⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⢿⣦⣤⣾⡆⣹⣿⣿⣿⡄⠹⣿⣿⠀⣿⣿⣿⠃⣸⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠗⢀⣿⡏⠀⣿⣿⡏⢠⣿⣿⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠸⢿⠿⠟⠋⠉⠁⠀⠐⠚⠛⠃⣰⣿⡿⠀⣾⣿⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⠿⠿⠃⣸⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣤⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''



deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = 21



def dealing_cards(card_deck):
    """Returns a list containing two random cards from the deck."""
    your_cards.extend(random.sample(card_deck, 2))
    cpu_cards.extend(random.sample(card_deck, 2))

    return (your_cards, cpu_cards)

def another_card(card_deck):
    """Adds a new random card to the given hand."""
    new_card = random.choice(card_deck)
    your_cards.append(new_card)
    return your_cards

def calc_score(hand):
    """Calculates the total score of a hand, adjusting Aces (11 to 1) if necessary."""
    total = sum(hand)

    while total > blackjack and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)

    return total

def pick_a_winner(n1, n2):
    """Compares scores and returns the string result of the match."""
    if n1 > 21:
            return f"Player: {n1} - You went over! 🤖 CPU wins!"
    elif n2 > 21:
            return f"CPU: {n2} - CPU went over! 🙍 You win!"
    elif n1 == n2:
            return "🙍 Draw 🤖"
    elif n1 > n2:
            return f"{n1} vs {n2} - 🙍 Player wins!"
    else:
            return f"{n1} vs {n2} - 🤖 CPU wins!"



def play_game():
    """Main game loop for Blackjack. Manages user input and game state."""
    global your_cards, cpu_cards
    your_cards = []
    cpu_cards = []

    start_game = input("Do you want to deal the cards? Type 'y' or 'n': ")

    if start_game.lower() == 'y':
        print(logo)
        dealing_cards(deck)

        player_points = calc_score(your_cards)
        cpu_points = calc_score(cpu_cards)

        print(
                f"Your deck {your_cards} - Total: {player_points}\n"
                f"Computer's first card: {cpu_cards[0]}\n"
        )

    if player_points < blackjack and cpu_points < blackjack:
        while True:
            another_card_option = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            
            if another_card_option == 'y':
                    another_card(deck)
                    player_points = calc_score(your_cards)
                    
                    print(f"Your deck {your_cards} - Total: {player_points}")
                    print(f"Computer's first card: {cpu_cards[0]}")

                    if player_points > blackjack:
                            print("You went over 21! You lose.")
                            break
                    elif player_points == blackjack:
                            print("Blackjack! 21!")
                            break

            elif another_card_option == 'n':
                    while calc_score(cpu_cards) < 17:
                            cpu_cards.append(random.choice(deck))
                    
                    cpu_points = calc_score(cpu_cards)
                    
                    print(f"\nYour final hand: {your_cards}, final score: {player_points}")
                    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_points}")
                    print(pick_a_winner(player_points, cpu_points))
                    break
            else:
                    print("Invalid option.")
    else:
        print(pick_a_winner(player_points, cpu_points))

    if input("\nDo you want to play again? 'y' or 'n': ") == "y":
        play_game()
    else:
          print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    play_game()