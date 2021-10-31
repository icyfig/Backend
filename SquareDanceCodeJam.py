#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 07:21:18 2020

@author: icy
"""

def main():
   test_cases = int(input())
   for iii in range(test_cases):
     N = input().strip()
     N_list = N.strip()
     R = N_list[0]
     C = N_list[1]
     data = []#data is a 2d array. of rows and columns. Each element represents a row
     for j in range(R):
        row = input().strip()
        row_list = row.split()
        for i in range(0, len(row_list)): 
           row_list[i] = int(row_list[i]) 
    
#        row_list_int = [int(i) for i in row_list]
#        row_list_tuple = tuple(i for i in row_list_int)
        data.append(row_list)
      
     
     ans = find_ans(data,R,C)
     output = "Case #"+str(iii+1)+": "+str(ans)
     print(output)

def find_ans(data,R,C):
   list_of_columns = []
   for i in range(C):
      temp_col = []
      for j in range(len(data)):
         temp_col.append(data[j][i])
      list_of_columns.append(temp_col)
      
      
      
   ilev = 0
   roundlev = 0
   while(True):
      roundlev = 0
      for i in data:
         temp = sum[i]
         roundlev += temp
      ilev += roundlev
      
      #Time to eliminate people
      #Check rowwise
      row_pos = -1
      remove_list_rowf = []#Each element is a list, representing columns.Each element of that is further a list of two-true,false
      remove_list_rowb = []
      remove_list_columnf=[]
      remove_list_columnb = []
      #Remove list contains a list of tuples-positions to remove
#      tlist = []
#      tflist = [False,False]
#      for i in range(C)
#      for i in range(len(data)):
#         remove_list.append()
#      previous_person = 0
      for i in data:
         row_pos += 1
         column_pos = -1
         for j in i:
            column_pos += 1
            if(j == 0):
               continue
            elif(j>=previous_person):
               previous_person = j
            else:
               #Also check if same is true of next row element
               if(column_pos == C-1):#If it is last position
                  remove_list_rowf.append([row_pos,column_pos])
               else:
                  nextt = data[row_pos][column_pos+1]
                  if(nextt>j):
                     remove_list_rowf.append((row_pos,column_pos))
#      data_row_rev = data[:]
#      for i in data_row_rev:
#         i.reverse()
         
      
      for i in remove_list_rowf:
         roww = i[0]
         columnn = i[1]
         itemm = data[roww][columnn]
         nexte = 0
         for i in range(columnn,C):
            if(data[row][i] == 0):
               continue
            else:
               nexte = data[row][i]
               break
         if(nexte>itemm):
            remove_list_rowb
         
                     
      
               
         
         