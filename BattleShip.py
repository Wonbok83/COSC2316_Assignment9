'''
Created on Apr 9, 2019

@author: wonbokyang
'''

import numpy as np
import random
#Apr 4 
#Battle ship 
x = 5
B1 = [['.']*x for i in range(x)]
r=random.randint(0,4)
c=random.randint(0,4)
#B1[r][c] ='*'
attackS =1


while(attackS <= 5):
    print("type coordinate where you want to move ship(between 0 - 4)")
    print("row:")
    r1 = int(input())
    print("Col:")
    c1 = int(input())
    if(r1 == r and c1 == c):
        print("You attack the ship")
        B1[r1][c1]="0"
        attackS=6
        for p in B1:
            print(p)
    else : 
        print("You miss the ship")
        print("You tried", attackS, "of 5")
        B1[r1][c1]="^"
        attackS+=1
       
        print("Try again")
        for p in B1:
            print(p)
