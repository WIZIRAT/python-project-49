import random


GAME_INSTRUCTION = 'What number is missing in the progression?'
MIN_PROGRESSION_LEN = 5
MAX_PROGRESSION_LEN = 10
MIN_STEP_LEN = 1
MAX_STEP_LEN = 10
MIN_START_NUM = 1
MAX_START_NUM = 100
START_NUM_HIDDEN_INDEX = 0


def generate_game():
    progression, correct_answer, hidden_index = generate_progression()
    progression[hidden_index] = '..'
    result = ' '.join(map(str, progression))
    return result, correct_answer


def generate_progression():
    progression_len = random.randint(MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN)
    hidden_index = random.randint(START_NUM_HIDDEN_INDEX, progression_len - 1)
    start_number = random.randint(MIN_START_NUM, MAX_START_NUM)
    step = random.randint(MIN_STEP_LEN, MAX_STEP_LEN)
    progression = []
    for i in range(progression_len):
        progression.append(start_number + step * i)
    correct_answer = str(progression[hidden_index])
    return progression, correct_answer, hidden_index
