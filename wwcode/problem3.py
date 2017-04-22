# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 00:33:35 2017

@author: Марианна
"""

s=str(input("Please, enter some string: "))
current=s[0]
final=''
for i in range(1,len(s)):
    if s[i]>=s[i-1]:
        current+=s[i]
        if len(final)<len(current):
            final=current
    else:
            current=s[i]
        
print("The longest substring in alphabetic order:", final)

