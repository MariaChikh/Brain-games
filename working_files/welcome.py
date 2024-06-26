#!/usr/bin/env python3
import prompt

def welcome_user():
    
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}')

if __name__ == 'main':
    welcome_user()
