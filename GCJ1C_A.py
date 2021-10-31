#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:38:49 2020

@author: icy
"""

def main():
   test_cases = int(input())
   for iii in range(test_cases):
     N = (input().strip())
     data = N.split()#data is a 2d array. of rows and columns
     x = int(data[0]) #East
     y = int(data[1])
     path = str(data[2])
     
     ans = find_ans(x,y,path)
     output = "Case #"+str(iii+1)+": "+str(ans)
     print(output)
     
def find_ans(x,y,path):
   ans_time = 0;
   times = []
   #Finding the main time it takes
   for i in range(len(path)):
      substr = path[0:i+1]
      n = 0
      e = 0
      for j in substr:         
         if(j == 'N'):
            n +=1
         elif(j =='S'):
            n -= 1
         elif(j == 'E'):
            e += 1
         else:
            e -= 1
      time_for_this_event = len(substr)
      north_pos = y+n
      east_pos = x + e
#      print("n = "+str(north_pos))
#      print("e = "+str(east_pos))
      time_demand_for_this = abs(north_pos)+abs(east_pos)
      if(time_demand_for_this>time_for_this_event):
         times.append(len(path)+5)
      else:
         times.append(time_for_this_event)
         
   ans_time = min(times)
   if(ans_time == len(path)+5):
      return "IMPOSSIBLE"
   else:
      return ans_time
      
   
main()