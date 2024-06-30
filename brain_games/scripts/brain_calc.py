#!/usr/bin/env python3
from random import randint, choice
from brain_games.scripts.engine import *

def main():
    name = welcome_user()

    print('What is the result of the expression?')

    k=0
    operation = ['+', '-', '*']
    while k < 3:
        question = (f'{randint(1, 100)} {choice(operation)} {randint(1 , 100)}')
        correct_answer = eval(question)
        gameplay(question)
        if int(answer) == correct_answer:
            correct_answer()
            k+=1
        else:
            lose()
            break
    if k==3:
        win()

if __name__ == '__main__':
    main()
