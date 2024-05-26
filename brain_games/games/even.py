from brain_games.core import game_logic
import random


INSTRUCTION_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    question = random.randint(1, 100)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result


def start_game_even():
    game_logic(get_question_answer, INSTRUCTION_EVEN)
