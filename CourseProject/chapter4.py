from random import choice
import gvars

def chapter4_start():
    print("look for clues to get artifact")
    print(gvars.inventory)
    print("get caught in a bear trap")
    print("loose health")
    gvars.health -= 10
    print("pulls bear trap off foot")
    gvars.inventory.remove("first aid kit")
    print(gvars.inventory)
    gvars.health =100
    print("you find herbs that brings your health back to 100")
    explore_jungle()



def explore_jungle():
    print("your loud screams from being trapped in bear trap has awakened yanomami tribe")
    print("yanomami tribe comes to see why are you here and wants war but is willing to bargin the bargin is give up inventory and help kill rival hunters",)
    choice = 1
    while choice != 3:
        choice = int(input("what do you want to do? \n1.give up inventory.\n2.go to war with yanomani tribe.\n3.help kill rival hunters."))
        if choice == 1:
            print("loose inventory")
            gvars.inventory
        if choice == 2:
            print("go to war with yanmani tribe to work by yourself")
        if choice == 3:
            print("help kill rival hunters and find the artifact")
            import chapter5
            chapter5.Chapter5()
#chapter4_start()




