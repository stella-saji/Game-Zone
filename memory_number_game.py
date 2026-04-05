import random
import time

level = 1

print("🧠 Number Memory Game")

while True:
    numbers = [str(random.randint(0, 9)) for _ in range(level)]
    sequence = " ".join(numbers)

    print("\nMemorize this:")
    print(sequence)

    time.sleep(2)
    print("\n" * 50)  # clear screen effect

    answer = input("Enter the sequence: ")

    if answer == sequence:
        print("✅ Correct!")
        level += 1
    else:
        print("❌ Wrong!")
        print("Correct sequence was:", sequence)
        print("You reached level", level)
        break
