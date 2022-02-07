# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:37:38 2022

@author: owner
"""

#count even and odd numbers in a series.
even = 0
odd = 0

numbers = input("Please enter in a list of comma seperated numbers: ")

numbersList = numbers.split(",")

for i in numbersList:
    if (int(i)%2 == 0):
        even+=1
    else:
        odd+=1
        
print("There are " + str(even) + " even numbers.\n")
print("There are " + str(odd) + " odd numbers. \n")