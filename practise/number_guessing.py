import random

print("Welcome to the number guessing game(❁´◡`❁)")
print("I'am thinking a number between 1 to 100\nTry to guess")

attempts = 0
number = random.randint(1,100)
while True:
    guess =  int(input("Enter Your Guess😊: "))
    attempts += 1
    
    if guess == number:
        print(f"You guess the number correct😁 in {attempts} attempts")
        break

    elif(guess>number):
        print("Too High😮! Think lower number")

    elif(guess<number):
        print("Too Low😮! Think higher number")

    else:
        print("Something Went Wrong🥲!")
    
