# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:49:15 2022

@author: owner
"""
import random

#guess number between 1 and 9
random.seed()
uInput = 0
ranNum = random.randint(1,9)

while (ranNum != uInput):
    
    uInput = input("Please guess a number between 1 and 9: ")
    
    uInput = int(uInput)
    
    if(ranNum > uInput):
            print("Too low!")
    elif(ranNum < uInput):
            print("Too High!")
    else:
            print("Well guessed!")
    
