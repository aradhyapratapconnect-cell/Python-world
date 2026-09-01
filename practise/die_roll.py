import random

while True:
    roll = input("Dice roll (yes/no): ")
    if roll == "yes":
        print("The number is", random.randint(1,6))

    else:
        break
