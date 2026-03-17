import random

# List of words
words = ["apple", "tiger", "chair", "robot", "pizza"]

# Randomly choose a word
chosen_word = random.choice(words)

# Create display with underscores
display = []
for letter in chosen_word:
    display.append("_")

# Game variables
lives = 6
guessed_letters = []

print("Welcome to Hangman!")

# Game loop
while lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")

# Final result
if "_" not in display:
    print("🎉 You won!")
else:
    print("💀 You lost!")
    print("The word was:", chosen_word)