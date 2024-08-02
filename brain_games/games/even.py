from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 100


def generate_question_and_answer():

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    number = randint(START, STOP)
    question = f'{number}'

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
