#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:15:20 2020

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
   ans = ""
   maxi = -1
   #finding maximum element in the string
   for i in original:
      if(int(i)>maxi):
         maxi = int(i)
         
   pos = original.find(maxi)
   ans = original[:pos]+put_p(maxi)+original[pos+1:]
   #To the right side
   
   

def add_p(stri):
   return str("("+stri+")")

def nestable_right(stri):
   layers = 0
   for i in stri[1:]:
      if(i == '('):
         layers += 1
      else:
         break
      
   num = int(stri[0])
   if(layers >= num):
      return True
   else:
      return False
   
def nestable_left(stri):
   stri_rev=''.join(reversed(stri))
   return nestable_right(stri_rev)

def put_p(stri):
   num = int(stri)
   for i in range(num):
      stri = add_p(stri)
      
   return stri
      
   
   