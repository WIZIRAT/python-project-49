import random

def get_question_answer():
    question = random.randint(1, 100)
    result = 'yes' if question % 2 == 0 else 'no'
    return question. result
