#!/usr/bin/env python3
import prompt


def welcome_user():

    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}')
    return name


def gameplay(question):

    print(f'Question: {question}')
    answer = (input('Your answer: '))
    return answer


def correct():
    print('Correct!')


def lose(answer, correct_answer, name):
    print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer} \n Let's try again, {name}!")


def win(name):
    print(f'Congratulations, {name}!')
