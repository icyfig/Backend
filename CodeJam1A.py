#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 06:42:21 2020

@author: icy
"""

def main():
   test_cases = int(input())
   for iii in range(test_cases):
     N = int(input().strip())
     data = []#data is a 2d array. of rows and columns
     for j in range(N):
        row = str(input().strip())
        data.append(row)      
     
     ans = find_ans(data)
     output = "Case #"+str(iii+1)+": "+str(ans)
     print(output)


def find_ans(data):
   common_str = ""
   ast = ""
   possible = True
   pos = -1
   for i in data:
      pos += 1
      i_rev = i[::-1]
      data[pos] = i_rev
      
   shortest_word_length = len(min(words, key=lambda word: len(word)))
   cpos = -1
   word_formed = ""
   cl = ""
   while(True):
      cpos += 1
      cl = data[0][cpos]
      all_are_asterix = False
      for i in data:
         if(cl != '*'):
            break
         cl = i[cpos]
         
      if(cl == '*'):
         all_are_asterix = True
         
      word_formed += cl
      for i in data:
         if(i[cpos])