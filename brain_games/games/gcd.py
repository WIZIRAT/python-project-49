import random
import math


GAME_INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    num_one = random.randint(1, 100)
    num_second = random.randint(1, 100)

    expression = (f'{num_one} {num_second}')
    result = str(math.gcd(num_one, num_second))
    return expression, result
