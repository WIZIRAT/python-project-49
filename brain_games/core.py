import prompt


def game_logic(question_and_answer, instruction):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!\n"
          f"{instruction}")
    for i in range(3):
        question, correct_answer = question_and_answer()
        user_answer = prompt.string(f"Question: {question}\n"
                               "Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print(f"Confratulations, {name}!")