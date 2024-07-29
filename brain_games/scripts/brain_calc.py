#!/usr/bin/env python3
from brain_games.engine import gameplay
from brain_games.games.calc import generate_question_and_answer


def main():

    description = 'What is the result of the expression?'
    gameplay(generate_question_and_answer, description)


if __name__ == '__main__':
    main()
