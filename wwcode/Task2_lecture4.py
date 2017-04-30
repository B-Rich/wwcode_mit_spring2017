#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:00:23 2017

@author: Marianna
"""

def reverse(str1):
    '''
    A function computes the reversal of a string.
    For example, reverse("I am testing") should return 
    the string "gnitset ma I".
    '''
    
    rev_str = str1[::-1]
    return rev_str

#str1 = input("Enter string for reversing: ")
#print("Your reversed string: ", reverse(str1))

def is_palindrome():
    '''
    A function recognizes palindromes (i.e. words that look the same 
    written backwards). For example, is_palindrome("radar") should return True.
    '''
    str = input("Enter some word and I'll say is it palindrome or not: ")
    if str[::1]==str[::-1]:
        print ("Yes!!! It's a palindrome!!!")
        return True
    else:
        print ("No... It isn't a palindrome!!!")
        return False
    
    
#is_palindrome()

def is_member (list1):
    ''' 
    A function takes a value (i.e. a number, string, etc) x 
    and a list of values a, and returns True if x is a member of a,
    False otherwise. (Note that this is exactly what the in operator does,
    but for the sake of the exercise you should pretend Python did not have
    this operator.)
    '''
    x = input("Please, enter some letter: ")
    for i in range(len(list1)):
         if x == list1[i]:
             print("Your input is in list ", list1)
             return True 
    return False

#list1 = ['s', 'a', 'b', 'c', 'e', 'q', 'r', 'y', 'o']    
#is_member(list1)
