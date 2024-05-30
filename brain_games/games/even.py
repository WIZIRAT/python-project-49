import random


GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def generate_game():
    question = random.randint(MIN_NUM, MAX_NUM)
    if is_even(question) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer


def is_even(question):
    if question % 2 == 0
        return True
    else:
        return False
