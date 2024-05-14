from brain_games.core import game_logic
import random
from brain_games.instruction import INSTRUCTION_GCD
import math


def find_gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    expression = f"{num1} {num2}"
    result = str(math.gcd(num1, num2))
    return expression, result


def start_game_gcd():
    game_logic(find_gcd, INSTRUCTION_GCD)