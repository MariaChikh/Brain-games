import prompt


ROUNDS = 3


def play(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_module.DESCRIPTION)

    for _ in range(ROUNDS):
        question, correct_answer = game_module.generate_question_and_answer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}"
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
