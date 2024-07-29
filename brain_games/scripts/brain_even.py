#!/usr/bin/env python3

from brain_games.engine import gameplay
from brain_games.games.even import generate_question_and_answer


def main():

    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    gameplay(generate_question_and_answer, description)


if __name__ == '__main__':
    main()
