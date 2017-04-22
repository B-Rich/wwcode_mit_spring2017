# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:55:04 2017

@author: Марианна
"""

n=0
s=str(input("Please, enter some string with word(s) 'bob': "))
word="bob"
len_word=len(word)
for i in range(len(s)):
    if s[i:i+len_word]==word:
        n+=1
print("Number of times bob occurs is: ", n)