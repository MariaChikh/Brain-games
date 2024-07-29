#!/usr/bin/env python3

from brain_games.engine import gameplay
from brain_games.games.gcd import generate_question_and_answer


def main():
    description = 'Find the greatest common divisor of given numbers.'
    gameplay(generate_question_and_answer, description)


if __name__ == '__main__':
    main()
