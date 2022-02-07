# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:09:37 2022

@author: owner
"""
multiples = []

for i in range(1500, 2700):
    if(i%7==0 and i%5 ==0):
        multiples.append(i)

print(multiples)