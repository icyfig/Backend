#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:49:21 2021

@author: icy
"""
stateg = ''

def main():
   global stateg
   test_cases = int(input())
   for iii in range(test_cases):
      full_inp_list=(input().strip()).split()
      #x=cj
      #y=jc
      X = int(full_inp_list[0])
      Y = int(full_inp_list[1])
      stateg = str(full_inp_list[2])
      #print("X="+str(X)+"  Y = "+str(Y) + "stateg="+stateg)
      ans = find_ans(X,Y)
      output = "Case #"+str(iii+1)+": "+str(ans)
      print(output)

def find_ans(x,y):
   global stateg
   cost = 0
   curr = 'blank'
   pos = -1
   print("X="+str(x)+"  Y = "+str(y) + "   stateg="+stateg)
   for i in stateg:
      print("X="+str(x)+"  Y = "+str(y) + "   stateg="+stateg)
      pos += 1
      if pos == 0:
         if i == 'C' or i == 'J':
            curr = i
            continue
         if i == '?':
            find_forward_replacement(pos,x,y)
            continue
      if i == 'C':
         curr = 'C'
         continue
      if i == 'J':
         curr = 'J'
         continue
      
      if i == '?':        
         if(pos == len(stateg)-1):
            print("Enter last")
            if(curr=='C'):
               if(x>0 or x==0):
                  stateg = stateg[:pos]+'C'
                  curr = 'C'
                  continue
               else:
                  stateg = stateg[:pos]+'J'
                  curr = 'J'
                  continue
            else:
               if(curr=='J'):
                  if(y>0 or y==0):
                     stateg = stateg[:pos]+'J'
                     curr = 'J'
                     continue
                  else:
                     stateg = stateg[:pos]+'C'
                     curr = 'C'
                     continue
         else:
            nextEl = stateg[pos+1:pos+2]
            if nextEl == '?':
               if(curr=='C'):
                  if(x>0 or x==0):
                     stateg = stateg[:pos]+'C'+stateg[pos+1:]
                     curr = 'C'
                     continue
                  else:
                     stateg = stateg[:pos]+'J'+stateg[pos+1]
                     curr = 'J'
                     continue
               else:
                  if(curr=='J'):
                     if(y>0 or y==0):
                        stateg = stateg[:pos]+'J'+stateg[pos+1:]
                        curr = 'J'
                        continue
                     else:
                        stateg = stateg[:pos]+'C'+stateg[pos+1:]
                        curr = 'C'
                        continue
                        
            if curr == 'C':
               if nextEl == 'C':
                  if(x+y>0 or x+y==0):
                     stateg = stateg[:pos]+'C'+stateg[pos+1:]
                     curr = 'C'
                     continue
                  else:
                     stateg = stateg = stateg[:pos]+'J'+stateg[pos+1:]
                     curr = 'J'
                     continue
               elif nextEl == 'J':
                  stateg = stateg = stateg[:pos]+'J'+stateg[pos+1:]
                  curr = 'J'
                  continue
            elif curr == 'J':
               if nextEl == 'J':
                  if(x+y>0 or x+y==0):
                     stateg = stateg[:pos]+'J'+stateg[pos+1:]
                     curr = 'J'
                     continue
                  else:
                     stateg = stateg[:pos]+'C'+stateg[pos+1:]
                     curr = 'C'
                     continue
               elif nextEl == 'C':
                  stateg = stateg[:pos]+'C'+stateg[pos+1:]
                  curr = 'C'
                  continue
   print("X="+str(x)+"  Y = "+str(y) + "   stateg="+stateg)
   pos2 = -1
   prev = 'Blank'
   for i in stateg:
      pos2 += 1
      if(prev=='Blank'):
         prev = i
         continue
      if(prev == 'C'):
         if(i=='C'):
            prev='C'
            continue
         else:
            prev = 'J'
            cost += x
            continue
      else:
         if(i=='C'):
            prev='C'
            cost += y
            continue
         else:
            prev='J'
            continue
         
   return cost
         
            
def find_forward_replacement(pos,x,y):
   global stateg
   if(stateg[(pos+1):(pos+2)] == '?'):
      find_forward_replacement(pos+1,x,y)
      find_forward_replacement(pos,x,y)
   else:
      if(stateg[(pos+1):(pos+2)] == 'C'):
         #replace with c or j?
         if(y>0 or y==0):
            stateg = stateg[:pos]+'C'+stateg[pos+1:]
         else:
            stateg = stateg[:pos]+'J'+stateg[pos+1:]
      else:
         if(x>0 or x==0):
            stateg = stateg[:pos]+'J'+stateg[pos+1:]
         else:
            stateg = stateg[:pos]+'C'+stateg[pos+1:]
      
      
   
      
      
main()