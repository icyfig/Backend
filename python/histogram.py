# -*- coding: utf-8 -*-
"""
Created on Thu May 30 05:41:05 2019

@author: 
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

#Part 1
def has_duplicates(s): #Parameter s is the string
    d = histogram(s)  #Creating a histogram of the frequencies of different characters in s
    
    