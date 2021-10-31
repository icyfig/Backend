#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:29:35 2020

@author: icy
"""

def main():
   test_cases = int(input())
   for iii in range(test_cases):
     N = int(input().strip())
     data = []#data is a 2d array. of rows and columns
     for j in range(N):
        row = input().strip()
        row_list = row.split()
        for i in range(0, len(row_list)): 
           row_list[i] = int(row_list[i]) 
    
#        row_list_int = [int(i) for i in row_list]
#        row_list_tuple = tuple(i for i in row_list_int)
        data.append(row_list)
      
     
     ans = find_ans(data)
     output = "Case #"+str(iii+1)+": "+str(ans)
     print(output)

def find_ans(data):
   numAct = len(data)#Number of activities
   track = []
   for i in range(numAct):
      track.append('F')
      
   #creatign a list of start times
   start = []
   for i in data:
      start.append(i[0])
      
      
   start_sorted = sorted(start)
   start_keys_sorted = sorted(range(len(start)), key=lambda k: start[k])
   
   #Assigning to C
   c_time = -1
   pos = -1
   for i in start_sorted:
      pos += 1
      if(i>=c_time):
         #assign to c
         act_pos = start_keys_sorted[pos] #getting the activity 'id'
         track[act_pos] = 'C'
         c_time = data[act_pos][1]#shift to end time
         
   #Assign to J
   j_time = -1
   pos = -1
   for i in start_sorted:
      pos += 1
      act_pos = start_keys_sorted[pos] #getting the activity 'id
      #check if i is already assigned
      if(track[act_pos] == 'C'):
         continue
      if(i>=j_time):
         track[act_pos] = 'J'
         j_time = data[act_pos][1]#set end time as current j_time
         
   ans = ""
   for i in track:
      if(i == 'F'):
         ans = "IMPOSSIBLE"
         break
      ans += str(i)
      
   return ans
      
      
main()
     
      
   