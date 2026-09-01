import random

options = ["rock","paper","scissor"]
computer = random.choice(options)

user = input("Enter Your Choice [from Rock ,Papaer ,Scissors]:")
print(f"Computer choose",computer)

if user == computer:
    print("Its a tie😒!")

elif(computer == "rock" and user == "paper") or \
    (computer == "paper" and user == "scissor") or \
    (computer == "scissor" and user == "rock"):
    print("You win😁😁")

else:
    print("You loss")
