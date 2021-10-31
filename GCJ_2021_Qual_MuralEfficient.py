#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:02:57 2021

@author: icy
"""

stateg = ''

def main():
   global stateg
   test_cases = int(input())
   for iii in range(test_cases):
      full_inp_list=(input().strip()).split()
      #x=cj
      #y=jc
      X = int(full_inp_list[0])
      Y = int(full_inp_list[1])
      stateg = str(full_inp_list[2])
      #print("X="+str(X)+"  Y = "+str(Y) + "stateg="+stateg)
      ans = find_ans(X,Y)
      output = "Case #"+str(iii+1)+": "+str(ans)
      print(output)

def find_ans(x,y):
   global stateg
   if(stateg[0] == '?'):
      next_char = ''
      for i in stateg:
         if(i=='?'):
            continue
         else:
            next_char=i
            break
      if(next_char==''):
         return 0
      stateg = str(next_char)+stateg[1:]
   prev = stateg[0]
   for i in range(len(stateg)):
      if(stateg[i] == '?'):
         stateg = stateg[:i]+prev+stateg[i+1:]
      else:
         prev = stateg[i]
   curr=''
   cost=0
   for i in stateg:
      if(curr==''):
         curr=i
         continue
      elif(curr=='C' and i=='J'):
         cost += x
      elif(curr=='J' and i=='C'):
         cost += y
      curr = i
   return cost
            
      
main()