#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 06:36:39 2021

@author: icy
"""

import math


def main():
   test_cases = int(input())
   for iii in range(test_cases):
      n = int(input())
      numbers = (input().strip()).split()
      pos = 0
      for i in numbers:
         numbers[pos] = int(numbers[pos])
         pos += 1
      ans = find_ans(numbers,n)
      output = "Case #"+str(iii+1)+": "+str(ans)
      print(output)

def find_ans(numbers,n):
   count = 0
   curr_num = 0
   prev_digits = -1
   for i in numbers:
      print(numbers)
#      print('prev = '+str(prev_digits))
      if(curr_num == 0):
         prev_digits = count_digits(i)
         curr_num += 1
         continue
      dig_count = count_digits(i)
      if(dig_count>prev_digits):
         curr_num += 1
         prev_digits = dig_count
         continue
      if(dig_count == prev_digits):
         if(i>numbers[curr_num-1]):
            curr_num+=1
            continue
         else:
            count += 1
            numbers[curr_num] = int(str(i)+'1')
            curr_num +=1
            prev_digits += 1
            continue
      if(dig_count < prev_digits):
#         print('prev = '+str(prev_digits)+ ' dig_count= '+ str(dig_count))
         prev_substring = int(str(numbers[curr_num-1])[:dig_count])
         if(prev_substring>i):
            numbers[curr_num]= int(str(i)+str((prev_digits-dig_count+1)*'0'))
            count += prev_digits-dig_count+1
            curr_num += 1
            prev_digits = dig_count+prev_digits-dig_count+1
            continue
         if(prev_substring == i):
            extra_portion = str(numbers[curr_num-1])[dig_count:]
            lead_zeroes = ''
            remaining = ''
            lead = True
            for f in extra_portion:
               if(f=='0' and lead):
                  lead_zeroes += '0'
               else:
                  lead = False
                  remaining += f
            if(remaining == ''):
               remaining = '0'
               lead_zeroes = lead_zeroes[:len(lead_zeroes)-1]
            len_extra = len(str(remaining))
            extraPlus = int(remaining) +1
            if(len(str(extraPlus))==len_extra):
               count += prev_digits-dig_count
               numbers[curr_num]=int(str(i)+str(lead_zeroes)+str(extraPlus))
               curr_num += 1
               continue
            else:
               count += prev_digits-dig_count+1
               numbers[curr_num]= int(str(i)+str((prev_digits-dig_count+1)*'0'))
               curr_num += 1
               prev_digits = dig_count+prev_digits-dig_count+1
               continue
               
#            len_extra = len(str(extra_portion))
#            extraPlus = extra_portion +1
#            if(len(str(extraPlus))==len_extra):
#               count += prev_digits-dig_count
#               numbers[curr_num]=int(str(i)+str(extraPlus))
#               curr_num += 1
#               continue
#            else:
#               count += prev_digits-dig_count+1
#               numbers[curr_num]= int(str(i)+str((prev_digits-dig_count+1)*'0'))
#               curr_num += 1
#               prev_digits = dig_count+prev_digits-dig_count+1
#               continue
               
               
#            last_digit_prev = int(str(prev_substring)[-1])
#            print("last_digit_prev= "+str(last_digit_prev))
#            if(last_digit_prev==9):
#               count += prev_digits-dig_count+1       
#               numbers[curr_num]= int(str(i)+str((prev_digits-dig_count+1)*'0'))
#               curr_num += 1
#               prev_digits = dig_count+prev_digits-dig_count+1
#               continue
#            else:
#               count += prev_digits-dig_count
#               numbers[curr_num]= int(str(str(prev_substring)[:len(str(prev_substring))-1])+str(last_digit_prev+1))
#               curr_num += 1
#               continue
         if(prev_substring < i):
            count += prev_digits-dig_count
            numbers[curr_num]= int(str(i)+(prev_digits-dig_count)*'0')
            curr_num += 1
            continue
            
#         nbla = 0
#         equal = False
#         for j in str(i):
#            prev_corresponding = str(numbers[curr_num-1])[nbla]
#            if()
#            nbla += 11
   print(numbers)
   return count
         
      
      
def count_digits(Number):
   Number = int(Number)
   Count = 0
   while(Number > 0):
      Number = Number // 10
      Count = Count + 1
   return Count

      
      
      
      
main()