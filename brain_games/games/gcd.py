import random
import math


GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 100


def generate_game():
    num_one = random.randint(MIN_NUM, MAX_NUM)
    num_second = random.randint(MIN_NUM, MAX_NUM)

    expression = (f'{num_one} {num_second}')
    result = str(math.gcd(num_one, num_second))
    return expression, result
