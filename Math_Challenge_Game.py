import random
import time

score = 0
start_time = time.time()

for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    
    answer = int(input(f"{a} + {b} = "))

    if answer == a + b:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")

end_time = time.time()

print("\nFinal Score:", score)
print("Time Taken:", round(end_time - start_time, 2), "seconds")
