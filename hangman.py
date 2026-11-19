
import random

# List of predefined words
words = ["python", "computer", "software", "keyboard", "programming"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
max_attempts = 6
wrong_attempts = 0

print("==============================")
print("        HANGMAN GAME")
print("==============================")

# Main game loop
while wrong_attempts < max_attempts:

    # Display the current word
    display_word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    print("Wrong attempts:", wrong_attempts)
    print("Remaining attempts:", max_attempts - wrong_attempts)

    # Get a letter from the player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct letter!")
    else:
        print("Wrong letter!")
        wrong_attempts += 1

    # Check whether the player has guessed the complete word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The correct word was:", secret_word)
        break

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")
