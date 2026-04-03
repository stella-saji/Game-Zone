import random

words = ["python", "coding", "game", "hangman", "developer"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("🎮 Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Used letters:", " ".join(used_letters))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("⚠️ Already guessed!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong!")

if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)
