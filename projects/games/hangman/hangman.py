# Hangman_______________________________________________________

import random


word_list = [
    "ocean", "bright", "mountain", "simple", "garden",
    "shadow", "journey", "friend", "winter", "brave",
    "thunder", "forest", "silver", "planet", "bridge"
]


def word_picked():
  """Selects a random word from the list."""
  return (random.choice(word_list))


def blanks_n(word):
  """Creates a list of underscores matching the word length."""
  return ["_"] * len(word)


def is_in_word(word, guess, display):
  """Updates the display list if the guess is correct."""
  for i, char in enumerate(word):
    if char == guess:
      display[i] = guess


# --- Game Setup ---
while True:
  random_word = word_picked()
  blanks = blanks_n(random_word)
  lives = 6
  guessed_letters = []

  print("\n" + "="*32)
  print("----- Welcome to Hangman! -----")
  print("="*32)
  print(f"You have {lives} lives.\n")
  print(f"{' '.join(blanks)}\n")


  # --- Main Game Loop ---
  while lives > 0:
    guess_a_letter = input('Guess a letter: \n').lower()

    # 1. Validation: Check if input is a single letter
    if len(guess_a_letter) != 1 or not guess_a_letter.isalpha():
      print("Invalid input. Please enter exactly ONE letter (no numbers).\n")
      continue

    # 2. Validation: Check if letter was already guessed
    if guess_a_letter in guessed_letters:
        print(f"You already guessed '{guess_a_letter}'. Try a different letter.\n")
        continue

    guessed_letters.append(guess_a_letter)
    print(f"Letters guessed: {', '.join(guessed_letters)}")

    # 3. Check if guess is in the word
    if guess_a_letter in random_word:
      print(f"Yes! {guess_a_letter} is in the word!\n")
      print("_"*32)
      print("\n")
      is_in_word(random_word, guess_a_letter, blanks)
    else:
      lives -= 1
      print(f"You lost a life. Remaining lives: {lives}. Try again.\n")
      print("_"*32)
      print("\n")


    print(f"Word: {' '.join(blanks)}\n")


    # 4. Check Win Condition
    if "_" not in blanks:
      print(f"Congratulation! The word was: {random_word}!\n")
      print("You won!")
      break


  # --- End Game ---
  if lives == 0:
    print("\n" + "x"*32)
    print(f"Game Over. The word was: {random_word}\n")


  # --- Ask to Restart ---
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break # This breaks the OUTER loop and exits the program