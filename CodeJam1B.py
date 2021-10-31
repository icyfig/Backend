#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:12:59 2020

@author: icy
"""
#Problem A
def main():
   test_cases = int(input())
   for iii in range(test_cases):
     ranlist = (input().strip()).split()
     x = int(ranlist[0])
     y = int(ranlist[1])
#     ans = find_ans(x,y)
     output = "Case #"+str(iii+1)+": "+str('W')
     print(output)

def find_ans(x,y):
   maxi = x+y+2
   possib = []
   used = []
   for i in range(maxi):
      possib.append(int(2**i))
      used.append("")
      
   #First populte for minimum direction. 
   fl = ""
   flo = ""
   f_bin = ""
   if(x<y):
      f_bin = bin(x).replace("0b", "")
      fl = 'E'
      flo = 'W'
   else:
      f_bin = bin(y).replace("0b", "")
      fl = 'N'
      flo = 'S'
   f_bin_rev = f_bin[::-1]
   index = -1
   for i in f_bin_rev:
      index += 1
      if(i == '1'):
         used[i] = fl
      
   sl = ""
   slo = ''
   s_bin = ""
   if(x<y):
      s_bin = bin(y).replace("0b", "")
      sl = "N"
      slo = "S"
   else:
      s_bin = bin(x).replace("0b", "")
      sl = 'E'
      slo = 'W'
   s_bin_rev = s_bin[::-1]
   power = -1
   ssum = 0
   for i in s_bin_rev:
      power += 1
      if(i =='1'):
         if(used[power] == ""):
            used[power] = sl
            ssum += 2**(power)
            
   
main()
   
   
   
      
      
      
      