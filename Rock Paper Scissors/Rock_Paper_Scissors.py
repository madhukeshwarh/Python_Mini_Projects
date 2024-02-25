import random
def play():
    user=input("enter your chice:'r' for rock 'p' for paper and 's' for scissors: ")
    comp=random.choice(['r','p','s'])

    if user==comp:
        return 'Its a Tie'
    if win(user,comp):
        return 'You won!'

    return 'You lost!'

def win(p1,p2):
    # r>s, s>p, p>r
    if (p1=='r' and p2=='s') or (p1=='s' and p2=='p') or(p1=='p' and p2=='r'):
        return True

print(play())
