# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:56:48 2017

@author: Marianna
"""

def vowel_or_not(vowel, char):
    '''
    A function takes a character (i.e. a string of length 1) and returns
    True if it is a vowel, False otherwise.
    '''
    if char in vowel:
        return True
    else:
        return False

#vowel = 'aeiou'
#char = input("Enter one letter, please: ")
#print(vowel_or_not(vowel, char))


def translate(str_for_translate):
    '''
    A function will translate a text into "rövarspråket" (Swedish for "robber's
    language"). That is, double every consonant and place an occurrence of "o" 
    in between. For example, translate("this is fun") should return the string 
    "tothohisos isos fofunon".
    '''
    consonant = 'bcdfghjklmnpqrstvwxyz'
    robber = ''
    for char in str_for_translate:
        robber += char
        if char in consonant:
            robber += 'o' + char
    return robber

#str_for_translate = input("Enter some text and I will translate a text into 'rövarspråket' (Swedish for 'robber's language'): ")
#print(translate(str_for_translate))

                            
def sums(numbers):
    '''
    A function sums all the numbers in a list of numbers
    '''
    sums = 0
    for char in numbers:
        sums += char
    return sums

def multiply(numbers):
    '''
    A function multiplies all the numbers in a list of numbers
    '''
    mult = 1
    for char in numbers:
        mult *= char
    return mult

numbers = [1, 2, 3, 4]
print(numbers)
print("The sum of all numbers in list is", sums(numbers))
print("The product of all numbers is", multiply(numbers))
    
        
