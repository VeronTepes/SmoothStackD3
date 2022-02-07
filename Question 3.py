# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:30:51 2022

@author: owner
"""

n=5

for i in range(1, n):
    for j in range (0, i):
        print("*", end="")
    print("\n")
        
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print("\n")