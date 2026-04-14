from alphabet import LETTERS


# Encrypt message function
def encrypt(original_text, shift_amount):
    encoded_text = ""
    # Convert to upper so 'abc' becomes 'ABC' and matches LETTERS
    for letter in original_text.upper():
        if letter in LETTERS:
            shifted_index = (LETTERS.index(letter) + shift_amount) % len(LETTERS)
            encoded_text += LETTERS[shifted_index]
        else:
            # If it's a space or symbol, just keep it
            encoded_text += letter

    print("_" * 33)
    print(f"Encoded message: {encoded_text}\n")

# Decrypt message function
def decrypt(original_text, shift_amount):
    decoded_text = ""
    # Reverse the shift
    shift_amount *= -1
    
    # Process the text the same way
    for letter in original_text.upper():
        if letter in LETTERS:
            shifted_index = (LETTERS.index(letter) + shift_amount) % len(LETTERS)
            decoded_text += LETTERS[shifted_index]
        else:
            decoded_text += letter

    print("_" * 33)
    print(f"Decoded message: {decoded_text}\n")

# --- App setup ---
print("=" * 33)
print("--- Welcome to Caesar Cipher! ---")
print("=" * 33)
print("\n")

while True:
  user_choice = input("Write 'ENCODE' for encrypting or 'DECODE' for decrypting. Write 'EXIT' to exit the program:\n").lower()
  print("_" * 33)
  
  if user_choice == "exit":
     print("=" * 33)
     print("----------- Good bye! -----------")
     print("=" * 33)
     break
  
  if user_choice == "encode":
    """Encrypt the message utilizing the shift number given"""
    text = input("Type your message: \n").upper()
    print("_" * 33)
    shift = int(input("Type the shift number: \n"))
    print("_" * 33)
    
    encrypt(text, shift)

  elif user_choice == "decode":
    """Decrypt the message utilizing the shift number given"""
    text = input("Type your message: \n").upper()
    print("_" * 33)
    shift = int(input("Type the shift number: \n"))
    print("_" * 33)
    
    decrypt(text, shift)

  else:
    print("Wrong option. You can only choose ENCODE or DECODE.")