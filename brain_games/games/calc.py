from brain_games.core import game_logic
import random
from brain_games.instruction import INSTRUCTION_CALC


def get_math_expression():
    num_one = random.randint(1, 100)
    num_second = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    expression = (f"{num_one} {operator} {num_second}")
    result = str(eval(expression))
    return expression, result


def start_game_calc():
    game_logic(get_math_expression, INSTRUCTION_CALC)
