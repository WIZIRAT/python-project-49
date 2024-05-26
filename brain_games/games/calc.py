import random


GAME_INSTRUCTION = 'What is the result of the expression?'


def generate_game():
    num_one = random.randint(1, 100)
    num_second = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    expression = (f'{num_one} {operator} {num_second}')
    if operator == '+':
        result = num_one + num_second
    elif operator == '-':
        result = num_one - num_second
    else:
        result = num_one * num_second
    return expression, result
