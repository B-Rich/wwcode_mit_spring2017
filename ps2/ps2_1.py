#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:36:23 2017

@author: Marianna K.
"""

import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.\n")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
  
number_of_guesses = 6
number_of_guessed_letters = 0
secret_word = choose_word(wordlist)
print("Hello! This is HANGMAAAAAN!!! Let's start! Good luck!\n")
print("You have a", str(number_of_guesses), "quesses. The secret word has", len(secret_word), "lowercase letters.")
guessed_letters= [] #empty list

while number_of_guesses > 0 and number_of_guessed_letters < len(secret_word):
    input_letter = input("Please, enter a letter (your guess): ")
    if input_letter in secret_word:
        print("You'r lucky! The letter is in word!")
        guessed_letters+=input_letter
            
        print(''.join([char if char in guessed_letters else ' _ ' for char in secret_word]))    
        if number_of_guessed_letters==len(secret_word):
                    print("You win!")
        
    else:
        number_of_guesses -= 1
        print("Ooops! You have", str(number_of_guesses), "guesses")
        if number_of_guesses == 0:
            print("Game over!")
            print("The word was", secret_word)
            
    

    



    
    


