import random
import sys

# Ensure emoji/unicode prints don't crash on Windows consoles using legacy encodings.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

def ask_yes_no(prompt: str) -> bool:
    """Return True for yes, False for no. Keeps asking until valid input."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please type yes/no (or y/n).")

def add_task():
    task = input("Enter a new task: ")
    with open("to_do.txt", "a") as f:
        f.write(task + "\n")
        print("Task added ✅")

def view_tasks():
    try:
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks found 📭")
            else:
                print("\n📝 Your To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found 📭")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        with open("todo.txt", "r") as f:
            tasks = f.readlines()

            if 1 <= task_no <= len(tasks):
                tasks.pop(task_no - 1)
                with open("to_do.txt", "w") as f:
                    f.writelines(tasks)
                    print("Task deleted 🗑️")
            else:
                print("Invalid task number ❌")
    except:
        print("Error deleting task ❌")

def number_guessing_game():
    print("Welcome to the number guessing game(❁´◡`❁)")
    print("Choose a difficulty level:")
    print("1. Easy   (numbers 1–50, 10 attempts)")
    print("2. Medium (numbers 1–100, 7 attempts)")
    print("3. Hard   (numbers 1–500, 5 attempts)")

    # Pick difficulty
    while True:
        level = input("Enter difficulty (1/2/3): ").strip()
        if level == "1":
            max_num = 50
            max_attempts = 10
            break
        elif level == "2":
            max_num = 100
            max_attempts = 7
            break
        elif level == "3":
            max_num = 500
            max_attempts = 5
            break
        else:
            print("Invalid choice ❌ Please enter 1, 2, or 3.")

    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts. Try to guess!")

    attempts = 0
    number = random.randint(1, max_num)

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess😊: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            print(f"You guessed the number correct😁 in {attempts} attempts")
            return
        if guess > number:
            print("Too High😮! Think a lower number")
        else:
            print("Too Low😮! Think a higher number")

    print(f"\nOut of attempts 🥲 The number was {number}. Better luck next time!")


def rock_paper_scissors_game():
    options = ["rock", "paper", "scissor"]
    computer = random.choice(options)

    user = input("Enter your choice [rock/paper/scissor]: ").strip().lower()
    if user not in options:
        print("Invalid choice ❌ Please type rock, paper, or scissor.")
        return

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie😒!")
    elif (computer == "rock" and user == "paper") or \
            (computer == "paper" and user == "scissor") or \
            (computer == "scissor" and user == "rock"):
        print("You win😁😁")
    else:
        print("You lose 😅")


def game():
    while True:
        print("1. Number Guessing Game")
        print("2. Rock, Paper and Scissor")
        print("3. Back")

        try:
            choice = int(input("Enter the choice for which game you want to play: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            while True:
                number_guessing_game()
                if not ask_yes_no("\nPlay number guessing again? (yes/no): "):
                    break

        elif choice == 2:
            while True:
                rock_paper_scissors_game()
                if not ask_yes_no("\nPlay rock/paper/scissor again? (yes/no): "):
                    break

        elif choice == 3:
            return

        else:
            print("Invalid choice ❌")

        if not ask_yes_no("\nDo you want to pick another game? (yes/no): "):
            print("Exiting game 👋")
            return


def truth_and_dare():
       
        truths = [
    "What is your biggest fear?",
    "What is your biggest secret?",
    "Who was your first crush?",
    "What is your most embarrassing moment?",
    "Have you ever lied to your best friend?",
    "What is something you’re bad at but wish you were good at?",
    "What’s the weirdest dream you’ve ever had?",
    "Who do you like the most right now?",
    "What’s the last thing you searched on Google?",
    "Have you ever cheated in a test?",
    "What’s the one thing you regret the most?",
    "What’s your biggest insecurity?",
    "Have you ever been caught doing something you shouldn’t?",
    "What’s the strangest habit you have?",
    "What’s your guilty pleasure?",
    "Who is the last person you stalked on social media?",
    "Have you ever broken something and blamed someone else?",
    "What’s the biggest lie you’ve told?",
    "What’s something you’ve never told anyone?",
    "What’s your biggest flex?",
    "Who do you trust the most?",
    "What’s your biggest weakness?",
    "Have you ever cried during a movie?",
    "What’s your worst fear in relationships?",
    "What’s the most awkward conversation you’ve had?",
    "Have you ever had a crush on a teacher?",
    "What’s your most useless talent?",
    "What’s the silliest thing you’re afraid of?",
    "What’s your worst habit?",
    "Who is your secret best friend?",
    "Have you ever pretended to like something you hate?",
    "What’s the most trouble you’ve ever been in?",
    "What’s your biggest dream?",
    "What’s the weirdest thing you’ve eaten?",
    "What’s your biggest turn-off?",
    "Who knows you the best?",
    "Have you ever cried in public?",
    "What’s the biggest rumor you’ve heard about yourself?",
    "What’s something you wish you could change about yourself?",
    "What’s your biggest motivation?",
    "Who do you miss the most?",
    "What’s your favorite memory?",
    "What’s the worst decision you’ve made?",
    "Have you ever lied to your parents?",
    "What’s your biggest jealousy?",
    "Who do you admire the most?",
    "What’s the most childish thing you still do?",
    "What’s your biggest fear about the future?",
    "What’s one thing you’d never do even for money?",
    "What’s your biggest achievement?",
    "What’s your favorite song right now?",
    "Who was the last person who made you laugh?",
    "What’s something you’re proud of but never talk about?",
    "What’s your biggest pet peeve?",
    "Have you ever been in love?",
    "What’s the dumbest thing you’ve ever done?",
    "What’s the most expensive thing you’ve ever bought?",
    "What’s your dream job?",
    "What’s something you’re scared to tell people?",
    "Who is your role model?",
    "What’s the best compliment you’ve ever received?",
    "What’s your biggest fear about failing?",
    "What’s the weirdest talent you have?",
    "What’s your favorite childhood memory?",
    "What’s the worst lie you ever told?",
    "What’s something you want to learn this year?",
    "Who do you talk to when you’re sad?",
    "What’s your biggest distraction?",
    "What’s the last thing that made you cry?",
    "What’s your biggest motivation in life?",
    "What’s your favorite food?",
    "What’s your least favorite subject?",
    "Who do you look up to the most?",
    "What’s the most awkward thing you’ve ever said?",
    "What’s your biggest dream for the future?",
    "What’s something you’ve never done but want to try?",
    "What’s your favorite movie?",
    "What’s the last secret you kept?",
    "What’s your biggest fear about growing up?",
    "What’s something that always makes you smile?",
    "What’s your favorite holiday?",
    "What’s the last lie you told?",
    "What’s something you’re really bad at?",
    "What’s your favorite app?",
    "What’s your biggest challenge right now?",
    "What’s the most childish thing you still enjoy?",
    "What’s something you wish people knew about you?",
    "What’s your biggest dream in life?",
    "What’s the one thing you can’t live without?",
    "What’s the nicest thing someone has ever done for you?",
    "What’s your biggest weakness in relationships?",
    "What’s your favorite hobby?",
    "What’s the last thing you regretted doing?",
    "What’s your biggest fear about success?",
    "What’s something you want to change about your routine?"
]

        dares = [
    "Do 10 push-ups",
    "Sing a song loudly",
    "Dance for 30 seconds",
    "Do your best animal impression",
    "Speak in a cartoon voice for one minute",
    "Send a funny emoji to someone",
    "Act like a robot for 30 seconds",
    "Do 15 jumping jacks",
    "Try to lick your elbow",
    "Say your name backwards",
    "Walk like a model for one minute",
    "Tell a joke right now",
    "Pretend you’re in a movie scene",
    "Do 20 squats",
    "Say the alphabet without moving your lips",
    "Make a funny face and hold it for 20 seconds",
    "Balance on one foot for 30 seconds",
    "Speak without using the letter A for one minute",
    "Do your best evil laugh",
    "Pretend to be your favorite celebrity",
    "Do 5 burpees",
    "Act like a baby for one minute",
    "Sing like a rockstar",
    "Do a slow-motion walk",
    "Say three nice things about yourself",
    "Pretend you’re a news reporter",
    "Do 25 jumping jacks",
    "Act like you’re underwater",
    "Speak in slow motion for one minute",
    "Pretend your phone is ringing and answer it",
    "Do 30 squats",
    "Act like a monkey",
    "Tell a scary story in 30 seconds",
    "Do 15 sit-ups",
    "Pretend you’re invisible",
    "Speak like a villain",
    "Do 40 jumping jacks",
    "Do your best superhero pose",
    "Act like you won the lottery",
    "Pretend you’re on a game show",
    "Do 20 lunges",
    "Make a beatbox sound",
    "Pretend to be a teacher",
    "Do your best zombie walk",
    "Say five animal names in five seconds",
    "Act like you’re on a red carpet",
    "Do 10 claps and 10 stomps",
    "Speak like a pirate",
    "Do a one-minute plank",
    "Take a deep bow like a king",
    "Talk in a whisper for one minute",
    "Walk backwards for 30 seconds",
    "Pretend to be a cat",
    "Do your best villain laugh",
    "Act like you’re on a runway",
    "Say the months of the year backwards",
    "Do five yoga poses",
    "Pretend you’re a superhero saving the world",
    "Do 20 high knees",
    "Talk like a baby for 30 seconds",
    "Act like you’re in a silent movie",
    "Do 15 toe touches",
    "Pretend you’re a famous YouTuber",
    "Do your best victory dance",
    "Say your favorite word ten times fast",
    "Walk like you’re stuck in slow motion",
    "Do 30 arm circles",
    "Pretend to be a chicken",
    "Tell a dramatic story",
    "Do 25 squats",
    "Act like a spy",
    "Do 20 push-ups against the wall",
    "Pretend you’re in a horror movie",
    "Do 10 sit-ups",
    "Make a silly noise every time you blink for 30 seconds",
    "Pretend to be a singer in a concert",
    "Do 15 jumping jacks with arms only",
    "Act like a video game character",
    "Do 30 seconds of shadow boxing",
    "Pretend to be a news anchor",
    "Do 20 calf raises",
    "Act like a cartoon character",
    "Do 10 burpees",
    "Pretend you’re in space",
    "Do 30 seconds wall sit",
    "Act like a magician",
    "Do 20 mountain climbers",
    "Pretend to be a DJ",
    "Do 30 seconds jumping in place",
    "Act like you’re stuck in an elevator",
    "Do 15 crunches",
    "Pretend to be a movie villain",
    "Do 20 jumping jacks with only legs",
    "Act like a zombie in slow motion"
]


        print("\n🎯 Welcome to Truth & Dare Game!")
        while True:
            choice = input("\nType 'truth', 'dare', or 'exit': ").strip().lower()

            if choice == "truth":
                print("👉 Your Truth is:", random.choice(truths))
            elif choice == "dare":
                print("👉 Your Dare is:", random.choice(dares))
            elif choice == "exit":
                print("Exiting Truth & Dare 👋")
                break
            else:
                print("Invalid choice ❌ Try 'truth' or 'dare'")
           


def calaculator():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back")

        try:
            choice = int(input("Enter the choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 5:
            return

        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        if choice == 1:
            print(a + b)
        elif choice == 2:
            print(a - b)
        elif choice == 3:
            print(a * b)
        elif choice == 4:
            if b == 0:
                print("Cannot divide by zero ❌")
            else:
                print(a / b)
        else:
            print("Invalid choice ❌")

        if not ask_yes_no("Calculate again? (yes/no): "):
            print("Exiting Calculator👋")
            return


while True:
    user = input("\nYou (type exit to exit the loop): ").lower()

    if user in ["hi", "hello", "hey", "yoo","hellow"]:
        replies = [
            "Hi there 😊",
            "Hello! Nice to see you 👋",
            "Hey! How can I help you today?",
            "Yoo! how can i help you "
        ]
        print("Arin:", random.choice(replies))

    elif user in ["how are you", "how r u"]:
        print("Arin: I'm doing great 😄 Thanks for asking!")

    elif user == "calculator":
        print("Arin: Sure! Let's calculate 🧮")
        calaculator()

    elif user == "game":
        print("Arin: Let's play a game 🎮")
        game()

    elif user == "to do list":
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")

            choice = input("Choose an option: ")

            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                delete_task()
            else:
                print("Invalid choice ❌")

    elif user == "truth and dare":
        truth_and_dare()  

    
    elif user == "help":
        print("Arin: You can type:")
        print("- hi / hello")
        print("- calculator")
        print("- game")
        print("- To Do List")
        print("- Truth and Dare")
        print("- exit")

    elif user in ["what what u can do","what can u do","what you can do"]:
        print("Arin: I can do ")
        print("- hi / hello")
        print("- calculator")
        print("- game")
        print("- To Do List")
        print("- Truth and Dare")
        print("- exit")


    elif user == "exit":
        print("Arin: Goodbye 👋 Have a nice day!")
        break

    else:
        print("Arin: Sorry, I didn't understand that 😕")

      
