#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:12:33 2020

@author: icy
"""

def main():
   test_cases = int(input())
   for i in range(test_cases):
     N = int(input().strip())#Number of peeks
     data = []#data is a 2d array. Each element is a list representing [plays,clears]
     for j in range(N):
        row = input().strip()
        row_list = row.split()#M, S, P
        for ik in range(0, len(row_list)): 
           row_list[ik] = int(row_list[ik]) 
    
        data.append(row_list)
      
     
     ans = find_ans(data)
     output = str(ans)
     print(output)
     
def find_ans(data):
   plays_list = []
   clears_list = []
   #cHECK if plays decreased
   for i in data:
      plays_list.append(i[0])
      clears_list.append(i[1])
   maxi = plays_list[0]
   for i in plays_list:
      if(int(i)>int(maxi)):
         maxi = int(i)
      elif(int(i)<int(maxi)):
         return 'NO'
      else:
         pass
      
   maxi2 = clears_list[0]      
   for i in clears_list:
      if(int(i)>int(maxi2)):
         maxi = int(i)
      elif(int(i)<int(maxi2)):
         return 'NO'
      else:
         pass
   
   for i in range(len(plays_list)):
      if(int(clears_list[i]>plays_list[i])):
         return 'NO'
      
   return 'YES'

main()
