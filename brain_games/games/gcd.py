from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 10


def generate_question_and_answer():

    a = randint(START, STOP)
    b = randint(START, STOP)
    question = f'{a} {b}'
    correct_answer = gcd(a, b)

    return question, str(correct_answer)
