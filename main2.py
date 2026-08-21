import random
n = random.randint(1,100)
guesses = 1
a = -1
while((a) != n):
    
    a = int(input("Guess a number: "))
    if(a>n):
        print("Lower number plz")
    elif (a<n):
        print("Higher number plz")
    guesses += 1
print(f"You have guessed the {n} number in {guesses} attempts")