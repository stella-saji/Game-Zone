import random

print("🎲 Dice Simulator")

while True:
    roll = input("\nRoll the dice? (y/n): ").lower()

    if roll == 'y':
        dice = random.randint(1, 6)
        print("You rolled:", dice)
    elif roll == 'n':
        print("Thanks for playing! 👋")
        break
    else:
        print("⚠️ Invalid input! Please enter y or n.")
