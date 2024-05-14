from brain_games.core import game_logic
import random
from brain_games.instruction import INSTRUCTION_CALC


def get_math_expression():
    num1 = random.randit(1, 100)
    num2 = random.randit(1, 100)
    operator = random.choice(['+', '-', '*'])

    expression = (f"{num1} {operator} {num2}")
    result = eval(expression)
    return expression, result


def start_game_calc():
    game_logic(get_math_expression, INSTRUCTION_CALC)