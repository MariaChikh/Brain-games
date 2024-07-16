from random import randint
from brain_games.scripts.engine import *


def main():
    name = welcome_user()

    print('What number is missing in the progression?')

    k = 0
    while k < 3:

        progression = []
        number = randint(1, 50)
        step = randint(3, 10)
        for _ in range(randint(5, 10)):
            progression.append(number)
            number = number + step
        correct_answer = progression[randint(0, len(progression) - 1)]
        correct_answer_index = progression.index(correct_answer)
        progression[correct_answer_index] = '..'
        question = (f'{progression}')
        answer = gameplay(question)

        if int(answer) == correct_answer:
            correct()
            k += 1
        else:
            lose(answer, correct_answer, name)
            break
    if k == 3:
        win(name)


if __name__ == '__main__':
    main()
