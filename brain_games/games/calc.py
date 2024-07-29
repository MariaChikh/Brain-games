from random import randint, choice


def generate_question_and_answer():

    operation = ['+', '-', '*']
    question = (f'{randint(1, 10)} {choice(operation)} {randint(1, 10)}')
    correct_answer = eval(question)
    return question, correct_answer
