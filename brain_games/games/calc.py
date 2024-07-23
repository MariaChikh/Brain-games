from random import randint, choice
from brain_games.engine import *


def brain_calc():
    name = welcome_user()

    print('What is the result of the expression?')


    def generate_question_and_answer():
        operation = ['+', '-', '*']
        question = (f'{randint(1, 10)} {choice(operation)} {randint(1 , 10)}')
        correct_answer = eval(question)
        answer = int(gameplay(question))
        return question, correct_answer, answer
    
    question, correct_answer, answer = generate_question_and_answer()
    check_answer(question, correct_answer, answer, name)
