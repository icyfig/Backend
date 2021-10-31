#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:03:10 2020

@author: Shubh
"""

def main():
   test_cases = int(input())
   for i in range(test_cases):
     N = (str(input().strip())).split()
     R = int(N[0])
     B = int(N[1])
     C = int(N[2])
     data = []#data is a 2d array. Each element is a list representing a C
     for j in range(C):
        row = input().strip()
        row_list = row.split()#M, S, P
        for i in range(0, len(row_list)): 
           row_list[i] = int(row_list[i]) 
    
        data.append(row_list)
      
     
     ans = find_ans(data,R,B,C)
     output = "Case #"+str(i+1)+": "+str(ans)
     print(output)

def find_ans(data,R,B,C):
   #First, weigh out the packing time into the scanning time. 
   data_safe = data[:]#Copy it before making changes
   R_safe = R
   robots_used = 0
   items_bought = 0
   scan_times = []
   answer_list = []#Length C. Each element is number of bits assigned to that counter
   for i in range(C):
      cash_list = data[i]
      pack_time = cash_list[2]
      max_allowed = cash_list[0]
      per_scan = cash_list[1]
      new_per_scan = per_scan + pack_time/max_allowed
      data[i][1] = new_per_scan
      scan_times.append(new_per_scan)
      
   #Let's make a list of counter scan times
      
   #Now find the minimum scan_time per article, and also.
   while(items_bought != B):#Till we don't buy everything we came for
      '''Pseudo code: 
         If first buy, purchase from least time one
         '''
      if(robots_used == R):
         pass
      else:
         if()
      