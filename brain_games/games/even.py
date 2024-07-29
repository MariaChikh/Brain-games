from random import randint


def generate_question_and_answer():

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    number = randint(1, 100)
    question = (f'{number}')

    if is_even(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
