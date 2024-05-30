import random


GAME_INSTRUCTION = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 100


def generate_game():
    num_one = random.randint(MIN_NUM, MAX_NUM)
    num_second = random.randint(MIN_NUM, MAX_NUM)
    operator = random.choice(['+', '-', '*'])

    expression = (f'{num_one} {operator} {num_second}')
    if operator == '+':
        result = num_one + num_second
    elif operator == '-':
        result = num_one - num_second
    elif operator == '*':
        result = num_one * num_second
    return expression, str(result)
