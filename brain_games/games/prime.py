from random import randint


def generate_question_and_answer():

    def is_prime(n):

        if n == 1:
            return True

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
