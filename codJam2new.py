#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:01:57 2020

@author: icy
"""

def main():
   #filepath = 'input.txt'
   test_cases = int(input())
      
   for i in range(test_cases):
     inps = str(input().strip())     
     ans = find_ans(inps)
     output = "Case #"+str(i+1)+": "+str(ans)
     print(output)

def find_ans(original):
   toclose = 0
   final = original
#   final = add_p(original[0])+original[1:]
#   toclose += int(original[0])
   pos = -1
   for i in original:
      pos += 1
#      if(i == "(" or ")"):
#         continue
      value = int(i)
      if(toclose == value):
#         print("inside equals. final = "+str(final))
         continue
      
      if(toclose<value):
         final = str(final[:pos])+str(add_p(i,value-toclose))+str(final[pos+1:])
#         print("inside value greater. final = "+str(final))
#         print("pos = "+str(pos))
         pos += value-toclose
         toclose += value-toclose
         
      else:
         final = str(final[:pos])+str(add_p_close(i,toclose-value))+str(final[pos+1:])
#         print("inside value lesser. final = "+str(final))
#         print("pos = "+str(pos))
         pos += toclose - value
         toclose -= toclose-value
         
         
   final += ")"*toclose
#   print(toclose)
      
   return final
   
def add_p(stri,p):
   for i in range(p):
      stri = "("+stri
   return stri

def add_p_close(stri,p):
   for i in range(p):
      stri = ")"+stri
   return stri
         
main()