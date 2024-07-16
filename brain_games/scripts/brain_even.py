#!/usr/bin/env python3

from random import randint
from brain_games.scripts.engine import *


def main():

    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    def is_even(number):
        if number%2 == 0:
            return True
        else:
            return False

    k = 0
    while k < 3:
        number = randint(1, 100)
        question = (f'{number}')
        answer = gameplay(question)

        if is_even(number) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    
        if is_even(number) is True and answer == 'yes':
            correct()
            k += 1
        elif is_even(number) is False and answer == 'no':
            correct()
            k += 1
        else:
            lose(answer, correct_answer, name)
            break
    if k == 3:
        win(name)

if __name__ == '__main__':
    main()
