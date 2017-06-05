# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:27:23 2017

@author: Марианна
"""

def sum_of_n(n):
    res = 0
    if n == 1:
        res += 1
        return res
    else:
        res = n+ sum_of_n(n-1)
        return res
n = int(input("Enter n: "))
print("The sum of all of the first n integers is", sum_of_n(n))
        