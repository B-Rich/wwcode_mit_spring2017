# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:10:45 2017

@author: Marianna
"""


def maps (words):
    '''
    A program maps a list of words into a list of integers representing
    the lengths of the correponding words.
    '''
    lengths = []
    for char in words:
        lengths.append(len(char))
    return lengths


def find_longest_word (words):
    '''
    A function takes a list of words and returns the length of the longest one.
    '''
    length = 0
    longest = ''
    for char in words:
        if len(char) > length:
            length = len(char)
            longest = char
    return longest


def filter_long_words(words, n):
    '''
    A function takes a list of words and an integer n and returns 
    the list of words that are longer than n.
    '''
    long_words = []
    for char in words:
        if len(char) > n:
            long_words.append(char)
    return long_words
              
    
    
    
n = 5    
words = ['apple', 'orange', 'banana', 'plum', 'pineapple', 'watermelon', 'melon', 'kiwi']
print("Our list of words", words)
print("Lengths of all words are", maps (words))
print("The longest word in list is", find_longest_word (words))
print("The words in list which longer then", n, "are", filter_long_words(words, n))