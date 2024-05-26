from brain_games.core import game_logic
import random
import math


INSTRUCTION_GCD = 'Find the greatest common divisor of given numbers.'


def find_gcd():
    num_one = random.randint(1, 100)
    num_second = random.randint(1, 100)

    expression = (f'{num_one} {num_second}')
    result = str(math.gcd(num_one, num_second))
    return expression, result


def start_game_gcd():
    game_logic(find_gcd, INSTRUCTION_GCD)
