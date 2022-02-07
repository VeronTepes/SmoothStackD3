# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:45:40 2022

@author: owner
"""

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(str(item) + "'s type is: " + str(type(item)))