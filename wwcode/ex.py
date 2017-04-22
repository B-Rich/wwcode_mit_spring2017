# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:31:21 2017

@author: Марианна
"""

iteration=0
while iteration<5:
    count=0
    for letter in "hello, world":
        count+=1
        if iteration%2==0:
           break
    print("Iteration " + str(iteration) + "; count is: " + str(count) )
    iteration+=1