from random import randint, choice
from brain_games.engine import welcome_user, check_answer


def brain_calc():
    name = welcome_user()

    print('What is the result of the expression?')

    def generate_question_and_answer():

        operation = ['+', '-', '*']
        question = (f'{randint(1, 10)} {choice(operation)} {randint(1 , 10)}')
        correct_answer = eval(question)
        return question, correct_answer

    check_answer(generate_question_and_answer, name)
