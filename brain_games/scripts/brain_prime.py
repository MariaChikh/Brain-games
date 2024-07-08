from random import randint
from brain_games.scripts.engine import *

def main():
    name = welcome_user()

    print ('Answer "yes" if given number is prime. Otherwise answer "no".')

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, (int(n**0.5) + 1)):
            if n % i == 0:
                return False
        return True

    k = 0
    while k < 3:

        number = randint(1, 100)
        question = (f'{number}')
        answer = gameplay(question)
        

        if  is_prime(number) == True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'


        if answer == correct_answer:
            correct()
            k+=1
        else:
            lose(answer, correct_answer, name)
            break
    if k==3:
        win(name)

if __name__ == '__main__':
    main()
