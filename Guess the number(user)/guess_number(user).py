import random
def computer_guess(n):
    low=1
    high=n
    feedback=''
    while feedback !='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} Too high(H) or Too low(L) or correct(c): ').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess-1
    print('Guess is correct')
computer_guess(10)
    
