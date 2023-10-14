import random as r
from time import sleep

def start(max, menu_func):
    guesses = 0
    guess = -1
    left, right = 1, max

    menu_func("Computer version")

    target = int(input("Target: "))
    while target > max:
        print(f"Target must not exceed {max}")
        target = int(input("Target: "))

    while True:
        guess = (left + right) // 2
        guesses += 1

        if guess == target:
            print(f"{guess}? YES")
            break

        if guess > target:
            right = guess - 1
        else:
            left = guess + 1

        print(f"{guess}? NO")
        sleep(1)
    
    print(f"Target {guess} found in {guesses} guesses")
