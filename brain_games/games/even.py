import random


GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    question = random.randint(1, 100)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result
