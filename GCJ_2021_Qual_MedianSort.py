#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:14:11 2021

@author: icy
"""

import math

def main():
   test_cases = int(input())
   n = int(input())
   q=int(input())
   for iii in range(test_cases):
      el = []
      el.append(1)
      el.append(2)
      el.append(3)
      curr=3
      middle = []
      print("1 2 3")
      response = int(input)
      if(response = 1):
         el = [2,1,3]
      elif(response = 2):
         el = [1,2,3]
      else:
         el=[1,3,2]
      
      middle_el=0
      while(True):
         curr += 1
         if(curr > n):
            print(" ".join(el))
            break
         middle = float(len(input_list))/2
         if middle % 2 != 0:
            middle_el = el[int(middle - .5)]
            left_of_middle = el[int(middle - .5)]
            print(str(left_of_middle)+' '+str(middle_el)+' '+nextEl)
            answer = int(input())
            if answer == left_of_middle:
               el
         else:
            print(str(el[int(middle)]) + ' ' + str(el[int(middle-1)])+' '+nextEL)
      
      
      
      
main()