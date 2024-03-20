import random
import restart
import gvars
def Chapter5():
    print("come across the artifact")
    print("kill the rival hunters or take artifact and run.")
    print("lets fight the rival hunters.")
def continue_game():
    import chapter1
    print("defeat rival hunters and turn in artifact or keep for respect")
    print("You have" , restart.money, "coins")
    restart.money += 10
    choice = input("Yes or No: ").lower()
    if choice == "yes":
        gvars.inventory=["map","gun","clothes","first aid kit","herbs"]
        chapter1.start_chapter_1()
    elif choice == "no":
        print("keep artifact for respect!")
    else:
        print("Invalid choice.")
        restart.restart_game()
