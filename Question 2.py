# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:13:22 2022

@author: owner
"""

#get inputs
tempFrom = input("Please enter the temperature scale you want to convert from (F or Fahrenheit, C for Celcius): ")
convTemp = input("Please enter in the temperature degree value that you want to convert from: ")
tempTo = ""
finalTemp = 0


#am I going F to c or c to f?
if(tempFrom == "F" or tempFrom == "f"):
    #convert f to c
    #c=5*((f-32)/9)
    tempTo = "C"
    finalTemp = 5*((float(convTemp)-32)/9)
    print(str(convTemp) + " Degrees " + tempFrom.capitalize() + " is " + str(finalTemp) + 
          " Degrees " + tempTo.capitalize())
    
else:
    #convert c to f
    #f = 9*(c/5)+32
    tempTo = "F"
    finalTemp = (9*(float(convTemp)/5))+32
    print(str(convTemp) + " Degrees " + tempFrom.capitalize() + " is " + str(finalTemp) + 
          " Degrees " + tempTo.capitalize())