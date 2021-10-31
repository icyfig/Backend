#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 01:24:18 2020

@author: icy
"""

def main():
   row = input().strip()
   row_list = row.split()
   T = int(row_list[0])
   B = int(row_list[1])
   for i in range(T):
      if(B%2 == 0):
            ans = handle_even(B)
      else:
            ans = handle_odd(B)
      print(ans,flush = True)
      if(i == T-1):#We finished solving the last test case
#         exit()
         pass
      else:
         if(input().strip() == 'Y'):
            continue
         else:
            exit()

def handle_even(B):
   positions_determined = 0
   positions = []
   for i in range(B):
      positions.append(-1)
   query_no = 0 #How many questions have been asked
   curr_pos_forward = 0#Zero-indexed
   curr_pos_backward = 0#Zero-indexed
   forward_time = True#Should I ask from forward or backward
   flipped = False
   reversedd = False
   
   while(positions_determined != B):
      #First checking if this is a quantum query
      if((query_no+1) %10 == 1 and (query_no+1) != 1):#It is a quantum query
         rev_pair_forward_index = -1#zero indexed
         old_rev = -1#rev stands for reverse
         old_flip = -1
         forwardxxx = False
         backwardxxx = False
         flip_poke_same = False
         old_flip_poke = False
         rev_poke_same = False
         flip_pair_forward_index = -1
         #Finding a pair of different digits to check later for reversal
         for i in range(len(positions)):
            if(positions[i] == -1 or positions[(len(positions)-1)-i] == -1):
               break#leaving the values at -1. There is no way to tell reversal. We shall later assume it to be no effec
            if(positions[i] != positions[(len(positions)-1)-i]):
               rev_pair_forward_index = i
               old_rev = positions[rev_pair_forward_index]
               break
            
         #Finding a pair of same numbers. This will help later in flip determination
         for i in range(len(positions)):
            if(positions[i] == -1 or positions[(len(positions)-1)-i] == -1):
               break#leaving the values at -1. There is no way to tell flip. Assume not.
            if(positions[i] == positions[(len(positions)-1)-i]):
               flip_pair_forward_index = i
               old_flip = positions[flip_pair_forward_index]
               break
            
         #Time to check for flip by asking query
         if(flip_pair_forward_index == -1):
            if(curr_pos_forward == curr_pos_backward):#Evenly done
               print(1,flush = True)#Asking for a random already known position
            elif(curr_pos_forward>curr_pos_backward):
               forwardxxx = True
               flip_poke_same = True
               old_flip_poke = positions[curr_pos_forward-1]#This is the poking element
               print(curr_pos_forward,flush = True)
            else:
               print(((B-1)-(curr_pos_backward-1))+1,flush = True)
               flip_poke_same = True
               backwardxxx = True
         else:
            print(flip_pair_forward_index+1,flush = True)
         temp_ans = int(input().strip())
         query_no += 1
         #If old flip is different from current, it can only be action of flip and not of reverse
         if(old_flip == -1):
            if(forwardxxx):
               positions[curr_pos_forward-1] = temp_ans#Simply change the changed element and pretend nothing happened
               flipped = False
            else:
               positions[((B-1)-(curr_pos_backward-1))] = temp_ans
         else:
            flipped = not(old_flip == temp_ans)
            
         if(old_rev == -1):
            if(curr_pos_forward == curr_pos_backward):#Evenly done
               print(1,flush = True)
               query_no += 1
               temp_ans_2 = int(input().strip())
               reversedd = False#Assume nothing done
            elif(curr_pos_forward>curr_pos_backward):
               rev_poke_same = True
               print(curr_pos_forward,flush = True)
               query_no += 1
               temp_ans_2 = int(input().strip())
               positions[curr_pos_forward-1] = temp_ans_2
               
            else:
               print(((B-1)-(curr_pos_backward-1))+1,flush = True)
               rev_poke_same = True
               query_no += 1
               temp_ans_2 = int(input().strip())
               positions[((B-1)-(curr_pos_backward-1))] = temp_ans_2
         else:
            #Ask for that reverse pos
            print(rev_pair_forward_index + 1,flush = True)
            new_rev_index = int(input().strip())
            query_no += 1           
            if(flipped):
               reversedd = (old_rev == new_rev_index)
            else:
               reversedd = not(old_rev == new_rev_index)
                  
         #Time to take appropriate action depending on the quantum nature
         if(flipped):#quantum - flipped
            tempp = -1
            for i in positions:
               tempp += 1
               if(i != -1):
                  if(positions[tempp] == 1):
                     positions[tempp] = 0
                  else:
                     positions[tempp] = 1
            
         if(reversedd):#Quantum- reversed
            #Reversing the positions list
            curr_pos_backward,curr_pos_forward=curr_pos_forward,curr_pos_backward
            forward_time = not(forward_time)
            rev_poss_list = [ele for ele in reversed(positions)]
            positions = rev_poss_list




      else:#Not a quantum query
         if(forward_time):#Forward turn
            print(curr_pos_forward+1,flush = True)
            pos = int(input().strip())
            curr_pos_forward += 1
            forward_time = False
            positions[curr_pos_forward-1] = pos
            query_no += 1
            positions_determined += 1
               
         else:#Backward Turn
            print(((B-1)-curr_pos_backward)+1,flush = True)
            pos = int(input().strip())
            positions[(B-1)-curr_pos_backward] = pos
            forward_time = True
            query_no += 1
            curr_pos_backward += 1
            positions_determined += 1
   #Returning answer
   answer = ""
   for i in positions:
      answer += str(i)
   return answer
         

def handle_odd(B):
#   ans = ""
   positions_determined = 0
   positions = []
   for i in range(B):
      positions.append(-1)
   query_no = 0 #How many questions have been asked
   middle_pos = B//2 + 1 #Non-zero indexed
   start_pos = 1#Non-zero indexed
   end_pos = B#Non-zero indexed
   middle = 0
   curr_pos_forward = 0#Zero-indexed
   curr_pos_backward = 0#Zero-indexed
   forward_time = True#Should I ask from forward or backward
   start = 0
   end = 0
   flipped = False
   reversedd = False
   
   while(positions_determined != B):#Asking queries until all positions are determined
      if(query_no == 0):
         #Ask for middle position
         print(middle_pos,flush = True)
         middle = int(input().strip())
         positions_determined += 1
         query_no += 1
         positions[middle_pos-1] = middle
         
      elif(query_no == 1):
         #Ask for start position
         print(start_pos,flush = True)
         start = int(input().strip())
         positions_determined += 1
         curr_pos_forward +=1
         query_no += 1
         positions[start_pos-1] = start
      
      elif(query_no == 2):
         #Ask for end position
         print(end_pos,flush = True)
         end = int(input().strip())
         curr_pos_backward += 1
         positions_determined += 1
         query_no += 1
         positions[end_pos-1] = end
         
      else: #Not the first query
         #First checking if this is a quantum query
         if((query_no+1) %10 == 1):#It is a quantum query
            rev_pair_forward_index = -1#zero indexed
            old_rev = -1
            #Finding a pair of different digits to check later for reversal
            for i in range(len(positions)):
               if(positions[i] == -1 or positions[(len(positions)-1)-i] == -1):
                  break#leaving the values at -1. There is no way to tell reversal. We shall later assume it to be no effec
               if(positions[i] != positions[(len(positions)-1)-i]):
                  rev_pair_forward_index = i
                  old_rev = positions[rev_pair_forward_index]
                  break
            #Asking for middle
            print(middle_pos,flush = True)
            new_middle = int(input().strip())
            query_no += 1
            flipped = not(middle == new_middle)
            if(old_rev == -1):
               reversedd = False #If undetereminable, then we assume it was not reversed
            else:
               #Ask for that reverse pos
               print(rev_pair_forward_index + 1,flush = True)
               query_no += 1
               new_rev_index = int(input().strip())
               if(flipped):
                  reversedd = (old_rev == new_rev_index)
               else:
                  reversedd = not(old_rev == new_rev_index)
                  
            #Time to take appropriate action depending on the quantum nature
            if(flipped):#quantum - flipped
               tempp = -1
               for i in positions:
                  tempp += 1
                  if(i != -1):
                     if(positions[tempp] == 1):
                        positions[tempp] = 0
                     else:
                        positions[tempp] = 1
            
            if(reversedd):#Quantum- reversed
               #Reversing the positions list
               curr_pos_backward,curr_pos_forward=curr_pos_forward,curr_pos_backward
               forward_time = not(forward_time)
               rev_poss_list = [ele for ele in reversed(positions)]
               positions = rev_poss_list
               
               
            
            
         else:#Not a quantum query
            if(forward_time):#Forward turn
               print(curr_pos_forward+1,flush = True)
               pos = input().strip()
               curr_pos_forward += 1
               forward_time = False
               positions[curr_pos_forward-1] = pos
               query_no += 1
               positions_determined += 1
               
            else:#Backward Turn
               print((B-curr_pos_backward)+1,flush = True)
               pos = input().strip()
               positions[(B-1)-curr_pos_backward]
               forward_time = True
               query_no += 1
               curr_pos_backward += 1
               positions_determined += 1
               
   #Returning answer
   answer = ""
   for i in positions:
      answer += str(i)
   return answer
      
main()