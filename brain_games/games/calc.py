from random import randint, choice
from brain_games.engine import *


def brain_calc():
    name = welcome_user()

    print('What is the result of the expression?')

    k = 0
    operation = ['+', '-', '*']
    while k < 3:
        question = (f'{randint(1, 10)} {choice(operation)} {randint(1 , 10)}')
        correct_answer = eval(question)
        answer = gameplay(question)
        if int(answer) == correct_answer:
            correct()
            k += 1
        else:
            lose(answer, correct_answer, name)
            break
    if k == 3:
        win(name)
