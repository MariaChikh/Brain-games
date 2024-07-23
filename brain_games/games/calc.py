from random import randint, choice
from brain_games.engine import welcome_user, gameplay, check_answer


def brain_calc():
    name = welcome_user()

    print('What is the result of the expression?')


    def generate_question_and_answer():
        operation = ['+', '-', '*']
        question = (f'{randint(1, 10)} {choice(operation)} {randint(1 , 10)}')
        correct_answer = eval(question)
        answer = int(gameplay(question))
        return answer, correct_answer
    
    answer, correct_answer = generate_question_and_answer()
    check_answer(generate_question_and_answer, name)
