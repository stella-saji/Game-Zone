import time
import random

sentences = [
    "Python is a powerful programming language",
    "Practice makes a person better every day",
    "Coding is like solving puzzles with logic",
    "Consistency is the key to improvement",
    "Small steps lead to big success"
]

sentence = random.choice(sentences)

print("⌨️ Typing Speed Game")
print("\nType the following sentence as fast as you can:\n")
print(sentence)

input("\nPress Enter when you're ready...")

start = time.time()
typed = input("\nStart typing:\n")
end = time.time()

time_taken = end - start

# Calculate accuracy
correct_chars = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

# Words per minute
wpm = (len(typed) / 5) / (time_taken / 60)

print("\n⏱️ Time:", round(time_taken, 2), "seconds")
print("🎯 Accuracy:", round(accuracy, 2), "%")
print("⚡ Speed:", round(wpm, 2), "WPM")
