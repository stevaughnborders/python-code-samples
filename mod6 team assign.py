#stevaughn borders
#02/27/2024
# find a number between 1 and 10

import secrets

prob = secrets.SystemRandom().randint(1,10)
#print(prob)
number=11
while prob!=number:
    number=int(input("enter a number betweeen 1 and 10"))
    if prob==number:
        print("well done")
    elif prob < number:
        print("guess lower")
    else:
        print("guess higher")

