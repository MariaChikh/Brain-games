#!/usr/bin/env python3
from brain_games.engine import gameplay
from brain_games.games.progression import generate_question_and_answer


def main():

    description = 'What number is missing in the progression?'
    gameplay(generate_question_and_answer, description)


if __name__ == '__main__':
    main()
