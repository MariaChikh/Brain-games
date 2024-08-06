from random import randint


DESCRIPTION = 'What number is missing in the progression?'
START = 1
STOP = 50
STEP_START = 3
STEP_STOP = 10
PROGRESSION_LENGTH_START = 5
PROGRESSION_LENGTH_STOP = 10


def generate_question_and_answer():

    progression = []
    number = randint(START, STOP)
    step = randint(STEP_START, STEP_STOP)
    for _ in range(randint(PROGRESSION_LENGTH_START, PROGRESSION_LENGTH_STOP)):
        progression.append(number)
        number = number + step
    correct_answer = progression[randint(0, len(progression) - 1)]
    correct_answer_index = progression.index(correct_answer)
    progression[correct_answer_index] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'
    return question, str(correct_answer)
