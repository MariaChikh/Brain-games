from random import randint
from brain_games.engine import welcome_user, check_answer


def brain_progression():
    name = welcome_user()

    print('What number is missing in the progression?')

    def generate_question_and_answer():

        progression = []
        number = randint(1, 50)
        step = randint(3, 10)
        for _ in range(randint(5, 10)):
            progression.append(number)
            number = number + step
        correct_answer = progression[randint(0, len(progression) - 1)]
        correct_answer_index = progression.index(correct_answer)
        progression[correct_answer_index] = '..'
        progression = ' '.join(map(str, progression))
        question = (f'{progression}')
        return question, correct_answer

    check_answer(generate_question_and_answer, name)
