#stevaughnborders
#03/16/2024
#create a while loop that initializes a counter at 0 and will run until the counter reaches 50.


counter = 0
tens = []

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("Values divisible by 10 up to 50:", tens)