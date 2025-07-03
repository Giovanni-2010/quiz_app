import json
import random

def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_quiz(questions):
    score = 0
    total = len(questions)

    # Shuffle questions so quiz order changes every time
    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}/{total}:")
        print(q['question'])

        if q['type'] == 'multiple':
            choices = q['choices']
            for idx, choice in enumerate(choices, start=1):
                print(f"  {idx}. {choice}")
            while True:
                try:
                    answer = int(input("Your answer (enter the number): "))
                    if 1 <= answer <= len(choices):
                        break
                    else:
                        print("Please enter a valid choice number.")
                except ValueError:
                    print("Please enter a number.")

            if choices[answer - 1] == q['right_answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q['right_answer']}")

        elif q['type'] == 'boolean':
            while True:
                answer = input("Your answer (True/False): ").strip().lower()
                if answer in ['true', 'false', 't', 'f']:
                    break
                else:
                    print("Please answer 'True' or 'False'.")
            correct_answer = q['right_answer'].strip().lower()
            if (answer.startswith('t') and correct_answer == 'true') or \
               (answer.startswith('f') and correct_answer == 'false'):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q['right_answer']}")
        else:
            print("Unknown question type. Skipping...")

    print(f"\nQuiz finished! Your score: {score}/{total} ({score/total*100:.2f}%)")

if __name__ == "__main__":
    questions = load_questions('questions.json')
    run_quiz(questions)
