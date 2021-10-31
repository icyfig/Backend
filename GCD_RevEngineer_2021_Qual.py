#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 09:56:23 2021

@author: icy
"""


import math


def main():
   test_cases = int(input())
   for iii in range(test_cases):
      inp = [int(x) for x in (input().strip()).split()]
      size = inp[0]
      cost = inp[1]
      ans = find_ans(size,cost)
      output = "Case #"+str(iii+1)+": "+str(ans)
      print(output)

def find_ans(size,cost):
   if(cost>upper_bound(size)):
      return 'IMPOSSIBLE'
   if(cost<size-1):
      return 'IMPOSSIBLE'
   left = True
   limit = int(size)-1
   to_spend = cost-(size-1)
   start = ""
   leftGap = 0
   rightGap = 0
   for i in range(1,size+1):
      start += (str(i))
   while(to_spend != 0):
      #print("Enter loop")
      #print(start)
      #print(" to_spend= "+str(to_spend))
      #print(" limit = "+str(limit))
      if(to_spend>=limit):
         #print("Enter Reverse")
         #print("   To spend: "+str(to_spend))
         if left:
            start = start[:leftGap] + start[leftGap:len(start)-rightGap][::-1] + start[len(start)-rightGap:]
            left = False
            to_spend -= limit
            limit = limit-1
            rightGap += 1
            #print("    Enter left. Start = "+start)
            #print("    Enter left. to_spend = "+str(to_spend))
            
         else:
            start=start[leftGap]+start[:-1]
            start = start[:leftGap] + start[leftGap:len(start)-rightGap][::-1]+ start[len(start)-rightGap:]
            left=True
            to_spend -= limit
            limit=limit-1
            leftGap += 1
      else:
         if left:
            #print("Enter left")
            start = start[:leftGap] + start[leftGap:len(start)-rightGap-limit+to_spend][::-1] + start[len(start)-rightGap-limit+to_spend:]
            to_spend = 0
            left = False
            rightGap += 1
         else:
            #print("Enter right")
            start = start[:leftGap+limit-to_spend] + start[leftGap+limit-to_spend:len(start)-rightGap][::-1]+start[len(start)-rightGap:]
            to_spend = 0
            left = True
            leftGap += 1
            
   #print(start)
   return (" ".join(start)).strip()            
            
   
   
   
      
def upper_bound(size):
   up = int(size)-1
   sum=up
   while(up>=1):
      sum+=up
      up -= 1
   return sum
main()