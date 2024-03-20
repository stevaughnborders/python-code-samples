import random
from gvars import *


def start_chapter_1():
    print("As he made it to the rainforest he began his search for the lost artifact.")
    print("he exit the boat and stare directly at the treacherous rainforest jungle.")
    # Outdoor Module
    explore_outside()
    # Start the game
    #start_game()
def explore_outside():
    import chapter2
    print("he stands on the beach. What would you like to do?")
    print("1. Look weapons, food,")
    print("2. Explore the surroundings")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("Chapter 2 goes here")
        chapter2.start_chapter_2()
    elif choice == "2":
        collect_inventory()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        #explore_beach()
def collect_inventory():
    print("hello world")
    coins_found = random.randint(1, 10)
    import chapter2
    print(f"You explore the surroundings and find {inventory} weapons!")
    chapter2.start_chapter_2()

