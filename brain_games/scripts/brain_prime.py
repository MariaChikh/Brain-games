#!/usr/bin/env python3

from brain_games.engine import gameplay
from brain_games.games.prime import generate_question_and_answer


def main():

    descript = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    gameplay(generate_question_and_answer, descript)


if __name__ == '__main__':
    main()
