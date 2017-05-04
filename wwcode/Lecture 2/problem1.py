# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:26:38 2017

@author: Марианна
"""

n=0
s=str(input("Please, enter some string: "))
vovels='aeiou'
for char in s:
    if char in vovels:
        n+=1
print("Number of vovels in you string: ", n)