from brain_games.core import game_even
import random
from brain_games.instruction import INSTRUCTION_EVEN


def get_question_answer():
    question = random.randint(1, 100)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result


def start_game_even():
    game_even(get_question_answer, INSTRUCTION_EVEN)