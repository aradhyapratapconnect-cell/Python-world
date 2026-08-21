import random

'''
1 for Rock
-1 for Paper
0 for Scissor
'''


computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (rock, paper, scissor): ").lower()
youdict = {"rock": 1, "paper": -1, "scissor": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissor"}
you = youdict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw!😒 ") 


else:
    if (computer ==-1 and you== 0):
        print("You Win!😁")

    elif(computer ==-1 and you== 1):
        print("You Lose!🥲")

    elif (computer ==1 and you== 0):
        print("You Lose!🥲")

    elif(computer ==1 and you== -1):
        print("You Win!😁")

    elif (computer ==0 and you== 1):
        print("You Win!😁")

    elif(computer ==0 and you== -1):
        print("You Lose!🥲")

    else:
        print("Something went wrong ")