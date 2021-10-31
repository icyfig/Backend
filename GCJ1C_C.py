#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:58:38 2020

@author: icy
"""
import math

def main():
   test_cases = int(input())
   for iii in range(test_cases):
     N = (input().strip())
     data = N.split()
     n = int(data[0]) 
     d = int(data[1])   
     angles = (input().strip()).split()
     count= -1
     for i in angles:
        count += 1
        angles[count] = int(i)
     ans = find_ans(n,d,angles)
     output = "Case #"+str(iii+1)+": "+str(ans)
     print(output)

def find_ans(n,d,angles):
   total_angles = tota(angles)
   max_angle = min(angles)
   myangle = 0   
   list_of_divisors = []
   for i in angles:
      list_of_divisors.append(Divisors(i))
   #Pseudo Code
   #For each divisor less than max angle, count how many slices have it, and how many slices will be produced if that is chosen
   #Filter out those divisors for which the slices produced is less than the diners
   #Among remaining slices, choose maximium angle
   #If the maximum is one, then the number of cuts is just the crude value
   d = {}
   for i in list_of_divisors:
      for j in i:
         if(j in d):
            d[j] += 1
         else:
            d[j] = 0
   for i in d: #deleting those divisors that produced insufficient slices
      slices = 0
      for j in angles:
         slices += j//i
      if(slices<d):
         del d[i]
   if(not d):
      return n-1
         
   max_val = -1
   max_key = -1
   for key,value in d.items():
      if(value>max_val):
         max_val = value
         max_key = key
         
   if(max_val == 1):
      return n-1
   
   slance = 0
   cuts = 0

   for i in angles:
      if(slance >= d):
         break
      if(i > max_val):
         pass
      elif(i == max_val):
         slance += 1
      else:
         if(i % max_val == 0):
            cuts += (i/max_val) -1
            slance += i/max_val
         else:
            slance += i//max_val
            cuts += i//max_val
            
   return cuts
   
      
   
def tota(angl):
   total = 0
   for i in angl:
      total += i
   return total

def Divisors(n) : 
    d = []
    i = 1
    while i <= n : 
        if (n % i==0) : 
            d.append(int(i)) 
        i = i + 1
    return d

def primeFactors(n): 
    prf = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        prf.append(int(2))
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            prf.append(int(i))
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        prf.append(int(n)) 
        
    return prf

main()
#print(Divisors(12))