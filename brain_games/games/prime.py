import random


GAME_INSTRUCTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
MIN_NUM = 0
MAX_NUM = 100


def generate_game():
    number = random.randint(MIN_NUM, MAX_NUM)
    if is_prime(number) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return number, correct_answer


def is_prime(number):
    if number == 1 or 0:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    else:
        return True
