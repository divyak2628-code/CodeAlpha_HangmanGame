import random

# Step 1: Word list with hints
words_with_hints = {
    "apple": "A red or green fruit.",
    "banana": "A long yellow fruit.",
    "cherry": "A small red fruit often used on cakes.",
    "grapes": "Small round fruits, can be green or purple.",
    "orange": "A citrus fruit rich in Vitamin C."
}

# Step 2: Choose a random word
word, hint = random.choice(list(words_with_hints.items()))
word_letters = list(word)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
score = 100  # Start with 100 points

print("🎮 Welcome to the Hangman Game!")
print(f"💡 Hint: {hint}")
print("_ " * len(word))

# Step 3: Main game loop
while wrong_guesses < max_wrong:
    guess = input("\n🔤 Guess a letter: ").lower()

    # Step 4: Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only a single alphabet letter.")
        continue

    # Step 5: Check for repeated guesses
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Step 6: Correct or wrong guess
    if guess in word_letters:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        score -= 10  # Deduct points for wrong guess
        print(f"❌ Wrong guess! Remaining tries: {max_wrong - wrong_guesses}")
        print(f"💯 Current Score: {score}")

    # Step 7: Display current progress
    display = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord: ", display)

    # Step 8: Check for win
    if all(letter in guessed_letters for letter in word_letters):
        print("\n🎉 You won! The word was:", word)
        print("🏆 Final Score:", score)
        break
else:
    print("\n😢 You lost! The correct word was:", word)
    print("💯 Final Score:", score)
