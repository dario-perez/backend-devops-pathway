from data import LETTERS, VALUES


def check_score(word):
  '''
  Calculates the total score of a word based on global lists.

  Args:
      word (str): Word given by players.

  Returns:
      int: Sum of the points of every letter in the word.
  '''
  total_score = 0

  for caracter in word:
    if not caracter.isalpha():
      continue
    
    index = LETTERS.index(caracter)
    letter_point = VALUES[index]
    total_score += letter_point
  
  return total_score   


def check_winner(score1, score2):
  '''
  Compares two scores and prints the result of the game.

  Args:
      score1 (int): Player 1 score.
      score2 (int): Player 2 score.
  '''
  print(f"\nPlayer 1: {score1} | Player 2: {score2}")

  if score1 == score2:
    print("Tie!\n")
  elif score1 > score2:
    print("Player 1 wins!\n")
  else:
    print("Player 2 wins!\n")


# --- Game Setup ---
print("=" * 30)
print("---- Welcome to Scrabble! ----")
print("=" * 30)
print("\n")


while True:
  player_1_word = input("Player 1: ").upper()
  player_2_word = input("Player 2: ").upper()

  player_1_score = check_score(player_1_word)
  player_2_score = check_score(player_2_word)

  check_winner(player_1_score, player_2_score)

  play_again = input("Would you like to play again? (y/n): \n").lower().strip()
  if play_again != 'y':
      print("Thanks for playing! Goodbye.")
      break
