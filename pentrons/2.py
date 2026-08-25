import random

question = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "Who developed Python programming language?": "Guido van Rossum",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Which data type is used to store text in Python?": "String",
    "What does CPU stand for?": "Central Processing Unit",
    "Which keyword is used to define a function in Python?": "def",
    "What is 9 x 7?": "63",
    "Which gas do plants absorb from the atmosphere?": "Carbon dioxide",
    "What is the square root of 81?": "9"
}

score = 0 
question_list = list(question.items())

random.shuffle(question_list)

for question ,correct_answer in question_list:
    print(question)
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    elif user_answer.strip() == "":
        print("You didn't provide an answer.")
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")

print(f"Your final score is: {score}/{len(question)}")