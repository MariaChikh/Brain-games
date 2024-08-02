import prompt
import sys


def play(func):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(func.DESCRIPTION)

    for _ in range(3):
        question, correct_answer = func.generate_question_and_answer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}"
                  f"\nLet's try again, {name}!")
            sys.exit()
    print(f'Congratulations, {name}!')
