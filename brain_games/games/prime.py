from brain_games.core import game_logic
import random


GAME_INSTRUCTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime():
    number = random.randint(1, 100)
    if number == 1:
        return number, "no"
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return number, "no"
    return number, "yes"
