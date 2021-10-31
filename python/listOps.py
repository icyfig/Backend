# -*- coding: utf-8 -*-
"""
Created on Fri May 24 03:39:51 2019

@author: Shubham Agrawal
"""

food = 'I seek creamy blueberry pancakes'
t = food.split()
print(t)
#Removing three elements:
t.pop(3)
print("List after pop(3):")
print(t)

del t[2]
print('List after del t[2]:')
print(t)

t.remove('I')
print("List after remove('I'):")
print(t)

#Sorting:
t.sort()
print("List after t.sort():")
print(t)

#Adding three elements:
t.append('me')
print("List after t.append('me'):")
print(t)

a = ['all','through','day']
t.extend(a)
print("List after t.extend(a):")
print(t)

t.insert(5, 'the')
print("List after t.insert(5, 'the'):")
print(t)

#Turning the list back to a string:
t = ' '.join(t)
print("List after ' '.join(t)")
print(t) #printing the string

