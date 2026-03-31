import random
import time

score = 0
start_time = time.time()

for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    
    while True:
        try:
            answer = int(input(f"Question {i+1}/5: {a} + {b} = "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if answer == a + b:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {a + b}\n")

end_time = time.time()

print("=" * 40)
print(f"Final Score: {score}/5")
print(f"Time Taken: {round(end_time - start_time, 2)} seconds")
print("=" * 40)
