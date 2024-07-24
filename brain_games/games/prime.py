from random import randint
from brain_games.engine import welcome_user, check_answer


def brain_prime():
    name = welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def generate_question_and_answer():

        def is_prime(n):

            for i in range(2, (int(n**0.5) + 1)):
                if n % i == 0:
                    return False
            return True

        number = randint(1, 100)
        question = (f'{number}')

        if is_prime(number) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        return question, correct_answer

    check_answer(generate_question_and_answer, name)
