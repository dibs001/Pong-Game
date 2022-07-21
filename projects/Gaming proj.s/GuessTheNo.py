import random
def guess(x):
    random_no=random.randint(1,x)
    guess=0
    while guess!=random_no:
        guess=int(input(f'Guess a no between 1 and {x}: '))
        if guess<random_no:
            print('Sorry,guess again.Too low.')
        elif guess>random_no:
            print('Sorry,guess again.Too high.')
    print(f'You have guessed the no. {random_no} correctly')
guess(2)
def comp_guess(x):
    low=1
    high=x
    feedback=''
    while (feedback!='c'):
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} too high (H),too low(L),or correct(C)?').lower()
        if (feedback=='h'):
            high=guess-1
        if feedback=='l':
            low=guess+1
    print(f'Congrats! The computer guessed your no. {guess} correctly!')
comp_guess(6)