from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
STOP = 100


def generate_question_and_answer():

    def is_prime(n):

        if n == 1 or n == 0:
            return False

        for i in range(2, (int(n**0.5) + 1)):
            if n % i == 0:
                return False
        return True

    number = randint(START, STOP)
    question = f'{number}'

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
