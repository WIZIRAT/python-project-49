import random


GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def generate_game():
    question = random.randint(MIN_NUM, MAX_NUM)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result
