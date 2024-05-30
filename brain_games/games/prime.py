import random


GAME_INSTRUCTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
MIN_NUM = 0
MAX_NUM = 100


def generate_game():
    number = random.randint(MIN_NUM, MAX_NUM)
    if number == 1 or 0:
        return number, 'no'
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return number, 'no'
    return number, 'yes'
