#guess the number

import random

while True:
    n=0
    a=random.randint(1,9)
    
    while True:
        n=n+1
        b=int(input('\nMake your guess (between 1-9)\n'))
        
        
        if (a==b):
            print("\nYou guess it right and you take {x} chances".format(x=n))
            c=input('Still wana play? (y/n)\n')
            if (c=='y' or c=='Y'):
                break
            else:
                print('thanks for playing')
                exit(0)
        else:
            pass
