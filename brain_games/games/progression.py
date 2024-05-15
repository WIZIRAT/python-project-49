from brain_games.core import game_logic
import random
from brain_games.instruction import INSTRUCTION_PROGRESSION


def get_progression():
    progression_len = random.randint(5, 10)
    hidden_index = random.randint(0, progression_len - 1)
    start_number = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = []

    for i in range(progression_len):
        progression.append(start_number + step * i)
    progression[hidden_index] = '..'
    result = ' '.join(map(str, progression))
    correct_answer = str(start_number + step * hidden_index)
    return result, correct_answer


def start_game_progression():
    game_logic(get_progression, INSTRUCTION_PROGRESSION)
