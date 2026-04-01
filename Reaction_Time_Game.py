import time
import random

input("Press Enter to start...")

wait_time = random.uniform(2, 5)

print("Wait for it...")

start = time.perf_counter()
time.sleep(wait_time)

print("NOW! Press Enter!")

start = time.perf_counter()
input()
end = time.perf_counter()

reaction_time = end - start

print("Reaction time:", round(reaction_time, 3), "seconds")
