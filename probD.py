#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:05:04 2020

@author: icy
"""

n = 3
inp = [[]]#length n representing rows. Inner list has n values representing columns.Each value is a list of two
out = [[]]#Outer = row, inner = column, value = letter or A = unassigned.
#Initialize to A

i_count = 0
for i in inp:
   j_count = 0
   for j in i:
      if(j == [-1,-1]):
         out[j[0]-1][j[1]-1] = 'X'
      j_count += 1
   i_count +=1
      
   
def there_a_way(start_row,start_column,end_row,end_column):#Does a path exist between start and end?#Indices list
   way = True
   current_row = start_row
   current_column = start_column
   if(start == end):
      return way
   while(True):
      if(start_row == end_row):
         pass
      if(start_row > end_row):
         
         
         
   
   
   