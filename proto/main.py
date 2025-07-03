import random

# quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "answer": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["1. Earth", "2. Mars", "3. Venus", "4. Jupiter"],
        "answer": 2
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["1. Elephant", "2. Giraffe", "3. Blue Whale", "4. Hippopotamus"],
        "answer": 3
    },
    {
        "question": "Which language is primarily spoken in Brazil?",
        "choices": ["1. Spanish", "2. Portuguese", "3. French", "4. English"],
        "answer": 2
    },
    {
        "question": "What is the result of 9 x 9?",
        "choices": ["1. 81", "2. 72", "3. 99", "4. 90"],
        "answer": 1
    }
]

# set the score 
score = 0

# loop through the questions
while True:
    # get random question and its choices
    random.shuffle(questions)
    q = random.choice(questions)

    question = q["question"]
    choices = q["choices"]
    answer = q["answer"]

    # print the question and choices
    print(f'\n {question} \n')
    for choice in choices:
        print(choice)

    # make sure user gives valid input
    while True:
        try:
            user_input = int(input("Enter your choice (1-4): "))
            if user_input in [1,2,3,4]:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # check if the answer 
    if user_input == answer:
        print(f"✅ Correct!\n {'-' * 30} \n")
        score += 10
    else:
        correct_choice = q["choices"][q["answer"] - 1]
        print(f"❌ Wrong! The correct answer was: {correct_choice}")
        print(f"{'-' * 30} \n")
        break

print(f"\n🎯 Final Score: {score}")
