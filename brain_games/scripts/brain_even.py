#!/usr/bin/env python3

from random import randint
from brain_games.scripts.welcome import welcome_user

def main():

    name=welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    def is_even(number):
        if number%2==0:
            return True
        else:
            return False

    k=0
    while k<3:
        number=randint(1, 100)
        print(f'Question: {number}')
        answer=input('Your answer: ')

        if is_even(number)==True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    
        if is_even(number) == True and answer == 'yes':
            print('Correct!')
            k+=1
        elif is_even(number) == False and answer == 'no':
            print('Correct!')
            k+=1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer} \nLet's try again, {name}!")
            break
    if k==3:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
