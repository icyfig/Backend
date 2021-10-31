#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:38:01 2020

@author: icy
"""

def main():
   test_cases = int(input().strip())
   for i in range(test_cases):
     N = input().strip()
     N_list = N.split()
     x = int(N_list[1])
     row = input().strip()
     row_list = row.split()#M, S, P
     for ik in range(0, len(row_list)): 
        row_list[ik] = int(row_list[ik]) 
    
     total_wealth = sum(row_list)
     print(int(total_wealth//x))
     
main()