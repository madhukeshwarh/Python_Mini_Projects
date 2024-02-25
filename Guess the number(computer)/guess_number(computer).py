import random
def guess(m,n):
    if m==n:
        print('unsuccessful attempt')
    else:
        rnumber=random.randint(m,n)
        guess=0
        while guess !=rnumber:
            guess=int(input(f'guess the number between {m} and {n}: '))
            if guess < rnumber:
                print('guess again.Too low')
            elif guess > rnumber:
                print('guess again.Too high')
        print('you have guessed the number correctly')
m=int(input('number starting from: '))
n=int(input('number upto: '))
guess(m,n)
