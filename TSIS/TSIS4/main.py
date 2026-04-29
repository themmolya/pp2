from ui import main_menu
from game import run_game

while True:
    action = main_menu()

    if action == "play":
        run_game()
    elif action == "quit":
        break