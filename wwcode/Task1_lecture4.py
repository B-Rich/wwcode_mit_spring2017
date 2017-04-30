# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 00:25:04 2017

@author: Марианна
"""

def max (x, y):
    '''
    Define a function max() that takes two numbers as arguments
    and returns the largest of them. Use the if-then-else construct
    available in Python. (It is true that Python has the max() function built in,
    but writing it yourself is nevertheless a good exercise.)
    '''
    if x > y:
        max = x
    else:
        max = y
    return max

#x = int(input("Enter the first number: "))
#y = int(input("Enter the second number: "))
#print("The largest number is: ", max(x, y))

def max_of_three (x, y, z):
    """
    Define a function max_of_three() that takes three numbers as arguments
    and returns the largest of them.
    """
    if x > y:
        if x > z:
            max = x
        else:
            max = z
    else:
        if y > z:
            max = y
        else:
            max = z
    return max

#x = int(input("Enter the first number: "))
#y = int(input("Enter the second number: "))
#z = int(input("Enter the third number: "))
#print("The largest number is: ", max_of_three (x, y, z))


def length_str(str1):
    '''
    Define a function that computes the length of a given string.
    (It is true that Python has the len() function built in,
    but writing it yourself is nevertheless a good exercise.)
    '''
    x = len(str1)
    return x

#str1 = input("Please, enter some string: ")
#x = length_str(str1)
#print("The lenght of your string is", x)


def lenght_list(list1):
    '''
    Define a function that computes the length of a given list. 
    (It is true that Python has the len() function built in,
    but writing it yourself is nevertheless a good exercise.)
    '''
    x = len(list1)
    return x

#list1 = [1, 2, 3, 4, 5]
#print("If you have some list, for exampe: ", list1)
#x = lenght_list(list1)
#print("The lenght of list is", x)


