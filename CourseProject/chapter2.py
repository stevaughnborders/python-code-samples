import gvars
import time
import chapter3
def start_chapter_2():
    print("walk around the beach. Chapter 2 begins...") # Placeholder for the next chapters content

    start_game()# Start the game
def start_game():
    print("the beach looks very abandoned with driftwood,seashells. player can see thunderstorms coming.")
    time.sleep(1)
    print("the ship was pulled in ashore in the sand to use as a escape from the jungle.")
    time.sleep(1)
    choice = 0
    while choice != 3:
        choice = int(input("What do you want to do? \n1. Look for supplies or materials.\n2.Look for clues about the location to the Hidden Temple.\n3.Look for a way into the jungle.\n"))
        if choice == 1:
            print("You find a bundle of bamboo shoots and palm leaves ready to be worked into anything you can think of. It's hard work getting them into your pack!")
            gvars.stamina -= 15
            gvars.inventory.append("sticks and leaves")
            print("Lose one stamina. Stamina is currently",gvars.stamina,".Lose all your stamina, and you'll die!")
        if choice == 2:
            print("you find tools,a note from a dead adventurer the note states")
            gvars.clues += 5
        if choice == 3:
            print("you look around the beach and see a opening clear to the jungle.")
            chapter3.start_chapter3()

