
def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= len(options):
                return answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def calculate_score(answers, correct_answers):
    score = 0
    for i in range(len(answers)):
        if answers[i] == correct_answers[i]:
            score += 1
    return score


def provide_feedback(user_answer, correct_answer, options):
    if user_answer == correct_answer:
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer was: {options[correct_answer - 1]}\n")


def quiz_game():
    
    questions = [
        "What is the capital of INDIA?",
        "Which language is used to develop this quiz?",
        "Which data structure is a collection of key-value INDIA?"
    ]

    options = [
        ["Berlin", "Madrid", "NEW DELHI", "Rome"],
        ["Java", "Python", "C++", "JavaScript"],
        ["List", "Tuple", "Dictionary", "Set"]
    ]

    correct_answers = [3, 2, 3]

    
    user_answers = []


    for i in range(len(questions)):
        user_answer = ask_question(questions[i], options[i])
        user_answers.append(user_answer)
        provide_feedback(user_answer, correct_answers[i], options[i])

    
    score = calculate_score(user_answers, correct_answers)
    print(f"Your final score is: {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()
