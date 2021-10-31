#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:48:31 2021

@author: icy
"""

import math

def main():
   test_cases = int(input())
   for iii in range(test_cases):
      list_length =int(input().strip())
      data= (input().strip()).split()
      count = -1
      for i in data:
         count += 1
         data[count] = int(i)
      ans = find_ans(data, list_length)
      output = "Case #"+str(iii+1)+": "+str(ans)
      print(output)

def find_ans(data, list_length):
   cost = 0
   for i in range(list_length-1):
      sublist = data[i:]
      min_index = sublist.index(min(sublist))
      j = min_index+i
      cost += (j-i+1)
      data = data[:i]+sublist[:min_index+1][::-1]+sublist[min_index+1:]
      
   return cost
      
      
main()