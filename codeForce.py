#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:16:12 2020

@author: icy
"""
guuu=input()
a = [int(h) for h in input().split()]
ans = 0

def good(a):#Assume length is atleast 3
   if(len(a) == 1):
      print("Boohooohoo wrong input")
      return False
   elif(len(a) == 2):
      gcdd = find_gcd(a[0],a[1])
      return not(gcdd == 1)
   
   leng = len(a)-1
   curr = 2
   first = a[1]
   second = a[2]
   gcd = find_gcd(first,second)
   while(True):
      if(curr == leng+1):
         break
      gcd = find_gcd(gcd,a[curr])
      
      curr += 1
      
   return not(gcd == 1)
      
      
      
      
   
def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 
 
def minops(a):
   #Assumption: negative numbers can be a multiple.(example: 2 is a divisor of -4)
   #Assumption: The number is not good.
   maximum = max(a)
   ops = max(a)+2#minimum of opsns
   
   for i in range(2,maximum+1):#numbers which are competing to be gcd
      #ops on each element:
      opsn = 0
      for j in a: #Making i the gcd of all list elements. No. of ops required for this = opsn
         
         #is i a factor of j
         if(j<i):
            jcop = j
            opsna = 0
            opsns = 0
            while(jcop<i):
               jcop += 1
               opsna += 1
            while(j%i != 0):
               j -= 1
               opsns += 1
               
            opsn += min(opsna,opsns)
            continue
         elif(j == i):
            continue
         
         else:
            jcop = j
            opsna = 0
            opsns = 0
            if(j%i == 0):
               continue
            while(jcop%i != 0):#addition
               jcop+=1
               opsna +=1
            while(j%i!=0):#subtraction
               j -= 1
               opsns += 1
               
            opsn += min(opsna,opsns)
            continue
               
               
         
               
            
         #if yes, continue
         #if no: keep adding 1 until it is; Keep subtracting 1 until it is; minimum of add and subtract as opsn
         #opsn represents minimum number of operations needed to make i the gcd(and hence the number good)
         
      ops = min(ops,opsn)
      
   return ops

def mainp():
   to_add = 0
   if(good(a)):
      ans = 0
   else:         
      count = 0
      for i in a:
         count +=1
         if(i==1):
            a[count] = 2
            to_add +=1
      ans = minops(a)+to_add
      
   return ans

ans = mainp()