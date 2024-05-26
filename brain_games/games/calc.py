import random


GAME_INSTRUCTION = 'What is the result of the expression?'


def generate_game():
    num_one = random.randint(1, 100)
    num_second = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    expression = (f'{num_one} {operator} {num_second}')
    result = str(eval(expression))
    return expression, result
