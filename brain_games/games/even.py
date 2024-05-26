import random


GAME_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    question = random.randint(1, 100)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result
