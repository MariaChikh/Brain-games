from random import randint
from brain_games.engine import *


def brain_gcd():
    name = welcome_user()

    print('Find the greatest common divisor of given numbers.')

    k = 0
    while k < 3:
        a = randint(1, 10)
        b = randint(1, 10)

        def gcd(a, b):

            while a != b:
                if a > b:
                    a -= b
                else:
                    b -= a
            return a
        question = (f'{a} {b}')
        answer = gameplay(question)
        correct_answer = gcd(a, b)

        if int(answer) == correct_answer:
            correct()
            k += 1
        else:
            lose(answer, correct_answer, name)
            break
    if k == 3:
        win(name)
