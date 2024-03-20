
def start_chapter3():
    choice=0
    import chapter4
    print("The tiger to defeat...")
    while choice != 1 and choice !=2:
        choice = int(input("\n1.Leave tiger alone.\n2.kill tiger.\n3.bait tiger with food.\n"))
        if choice == 1:
            print("you would not get a chance to win coins")
            chapter4.chapter4_start()

        if choice ==2:
            print("collect coins")
            chapter4.chapter4_start()
        if choice ==3:
            print("to esacpe form the tiger")

