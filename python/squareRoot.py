# -*- coding: utf-8 -*-
"""
Created on Mon May 13 03:57:19 2019

@author: 
"""
import math
def my_sqrt(a):
    x = 2.0 #Random starting value for x
    while True: #From textbook
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y 
    return y


def test_sqrt():
    a = 1
    while(a<=25):#Runs till 25
        diff = abs(my_sqrt(a)-math.sqrt(a)) # Absolute value of difference
        print('a = '+str(a)+' | '+'my_sqrt(a) = '+str(my_sqrt(a))+' | math.sqrt(a) = '+str(math.sqrt(a))+' | diff = '+str(diff))
        a += 1 #Incremmenting a
        
        
test_sqrt()