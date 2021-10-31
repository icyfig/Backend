#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:06:12 2020

@author: icy
"""

for _ in range(int(input())):
   ignore_this_var,max_marks=[int(h) for h in input().split(' ')]
   array_of_marks=[int(h) for h in input().split(' ')]
   sum_of_marks = sum(array_of_marks)
   ans = 0
   if(sum_of_marks < max_marks):
      ans = sum_of_marks
   else:
      ans = max_marks
      
   print(ans)