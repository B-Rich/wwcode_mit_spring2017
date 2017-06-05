# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:43:19 2017

@author: Марианна
"""

def factor(n):
    if n == 1:
        return 1
    else:
        return n*factor(n-1)
    
def Pascals_triangle(n):
    line = []
    for i in range(n):
        if i == 0:
            line = [1]
            print(line)
            continue
        if i == 1:
            line.append(1)
            print(line)
            continue
        if i == 2:
            line.insert(1, 2)
            print(line)
        if i == 3:
                line.insert(0, 1)
                line.insert(i, 1)
                line.insert(1, i)
                line.insert(i-1, i)
        if i >= 4:
            line.insert(0, 1)
            line.insert(i, 1)
            line.insert(1, i)
            line.insert(i-1, i)
            for i in range(2, i-1):
                linem = int((factor(n)/(factor(i)*factor(n-i))))
                line.insert(i, linem)
        print(line)
            
n = int(input("n = "))
Pascals_triangle(n)
    
 
#    
#n = int(input("n = "))
#print(factor(n))

