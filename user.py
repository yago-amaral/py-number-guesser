import random as r

def start(max, menu_func):
    target = r.randint(1, max)
    guesses = 0
    guess = -1

    menu_func("User version")

    while True:
        guess = int(input(f"Try #{guesses + 1}: "))
        guesses += 1

        get_hint(target, guess)

        if guess == target:
            break
    
    print(f"CONGRATULATIONS! You took {guesses} tries!")

def get_hint(target:int, guess:int):
    if target > guess:
        print(f"? > {guess}")
    else:
        print(f"? < {guess}")
