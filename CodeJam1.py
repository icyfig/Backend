#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:50:53 2020

@author: icy
"""

def main():
   filepath = 'input.txt'
   test_cases = 0
   with open(filepath) as fp:
      line = fp.readline()
      test_cases = int(line.strip())
      
      for i in range(test_cases):
         N = int(fp.readline().strip())
         data = []#data is a 2d array. of rows and columns
         for j in range(N):
            row = fp.readline().strip()
            row_list = row.split()
            data.append(row_list)
         
         k,rows,columns = find_ans(data)
         output = "Case #"+str(i+1)+": "+str(k) + " "+str(rows)+" "+str(columns)
         print(output)
            
         
      
def find_ans(data):
   #This method finds trace, r and c
   #finding trace
   curr = 0
   trace = 0
   for i in data:
      trace += int(i[curr])
      curr += 1
      
   #seeing how many rows have repeat elements
   rows = 0
   for i in data:
      if(duplicate(i)):
         rows += 1
   
   #seeing how many columsn have repeat elements:
   #Creating a list of list of columns
   curr2 = 0
   list_of_columns = []
   while(curr2 != curr):
      column = []
      for i in data:
         column.append(i[curr2])
      list_of_columns.append(column)
      curr2 += 1
      
   columns = 0
   for i in list_of_columns:
      if(duplicate(i)):
         columns += 1
   
   return (trace,rows,columns)
      
def duplicate(lis):
   for elem in lis:
      if lis.count(elem) > 1:
         return True
   return False

if __name__ == "__main__":main() ## with if