#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:26:04 2020

@author: icy
"""
import random

#Problem A
def main():
   test_cases = int(input())
   for iii in range(test_cases):
     ranlist = (input().strip()).split()
     x = int(ranlist[0])
     y = int(ranlist[1])
     ans = find_ans(x,y)
     output = "Case #"+str(iii+1)+": "+str(ans)
     print(output)

def find_ans(x,y):
   pass

def summ(st):
   x = 0
   y = 0
   power = -1
   for i in st:
      power += 1
      if(i == 'E'):
         x += 2**(power)
      elif(i == 'W'):
         x -= 2**(power)
      elif(i == 'N'):
         y += 2**(power)
      elif(i == 'S'):
         y -= 2**(power)
         
def rand():
   bla = random.randint(1, 4)