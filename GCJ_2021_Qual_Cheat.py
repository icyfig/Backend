#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:40:21 2021

@author: icy
"""

import math


def main():
   test_cases = int(input())
   probability = int(input())
   for iii in range(test_cases):
      results = []
      for i in range(2):
         results.append([int(x) for x in (" ".join(input()).strip()).split()])
   
      ans = find_ans(results)
      output = "Case #"+str(iii+1)+": "+str(ans)
      print(output)

def find_ans(results):
   #Assigning difficulty scores
   difficulty = []
#   print("results="+str(results))
   for i in range(5):
      sumg=0
      for j in results:
#         print("j="+str(j))
         sumg += j[i]
      difficulty.append(sumg)
   
   #Normalizing the difficulties
   for i in range(5):
      difficulty[i]=((difficulty[i]/2)*6)-3
   
   #Finding skill level, by average skill level solved.
   
   skill=[]
   for i in results:
      sumj=0
      for j in range(5):
         sumj+=i[j]*difficulty[j]
      skill.append(sumj/sum(i))
      
#      res_list = [i[j] * difficulty[j] for j in range(len(difficulty))]
#      skill.append(sum(res_list))
   deviations = []
   #Find deviation from sigmoid for each person by sd formula
   for i in range(2):
      person = results[i]
      sumk = 0
      for j in range(5):
         skillP = skill[i]
         difficultyP = difficulty[j]
         actual = person[j]
         sumk += dev(skillP, difficultyP, actual)
      deviations.append(math.sqrt(sumk/5))
      
#   print(deviations)
   deviations_index = sorted(range(len(deviations)), key=lambda k: deviations[k])
   return (deviations_index[1]+1)
      
def dev(s,d, actual):
   return (sigmoid(s-d)-actual)**2
def sigmoid(x):
   return (1/(1+(math.e**(-x))))
      

      
      
   
#   prob = []
#   n = 10000
#   p=0.5
#   for i in range(1,101):
#      x=sum(results[i])
#      bp = (ncr(n,x))*(p**x)*(1-p)**(n-x)
#      prob.append(int(bp))
#   print(str(prob))
#      
#def ncr(n, r):
#   return (math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
      
main()