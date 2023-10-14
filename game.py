import user, computer

def menu(msg: str):
    print("-" * 30)
    print(f"{'Number Guesser':^30}")
    print("-" * 30)

    print(f"{msg}\n")

game = computer if input("Game version(user/computer): ").lower() == "computer" else user
max_value = int(input("Max value: "))

game.start(max=max_value, menu_func=menu)
