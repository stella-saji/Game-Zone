# M = Missionaries, C = Cannibals

left_m = 3
left_c = 3
boat = "left"

def print_state():
    print(f"\nLeft -> M:{left_m} C:{left_c} | Right -> M:{3-left_m} C:{3-left_c} | Boat: {boat}")

def is_valid(m, c):
    # missionaries should not be outnumbered
    if m > 0 and c > m:
        return False
    if (3 - m) > 0 and (3 - c) > (3 - m):
        return False
    return True

while True:
    print_state()

    if left_m == 0 and left_c == 0:
        print("🎉 You solved it!")
        break

    try:
        m = int(input("Enter missionaries to move: "))
        c = int(input("Enter cannibals to move: "))
    except ValueError:
        print("⚠️ Enter valid numbers!")
        continue

    if m + c == 0 or m + c > 2:
        print("⚠️ You can move 1 or 2 people only!")
        continue

    if boat == "left":
        new_m = left_m - m
        new_c = left_c - c
    else:
        new_m = left_m + m
        new_c = left_c + c

    if new_m < 0 or new_c < 0 or new_m > 3 or new_c > 3:
        print("⚠️ Invalid move!")
        continue

    if not is_valid(new_m, new_c):
        print("💀 Missionaries got eaten! Game Over.")
        break

    left_m = new_m
    left_c = new_c
    boat = "right" if boat == "left" else "left"
