from random import randint


def generate_question_and_answer():

    a = randint(1, 10)
    b = randint(1, 10)

    def gcd(a, b):

        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    question = (f'{a} {b}')
    correct_answer = gcd(a, b)

    return question, correct_answer
