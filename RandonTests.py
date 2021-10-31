#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:47:03 2021

@author: icy
"""
a = [1,2,3]
b = [1,5,6]
res_list = [a[i] * b[i] for i in range(len(a))]
print(sum(res_list))