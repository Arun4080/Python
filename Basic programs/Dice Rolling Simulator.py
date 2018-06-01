# dice rolling simulator 1

import random

while True:
    a=input('\nWana roll dice (y/n)\n')

    if (a=='y' or a=='Y') :
        b=random.choice([1,2,3,4,5,6])
        print("you got "+str(b))   
        
    elif (a=='n' or a=='N'):
        exit(0)
    else: print("please try again \n")

    
        
        
