# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:35:39 2022

@author: owner
"""

#word reverse:
    
word = input("Please enter in a word: ")
revWord = ""

for index in range(0,len(word)):
    revWord += word[(len(word)-1-index)]
    

print(revWord)