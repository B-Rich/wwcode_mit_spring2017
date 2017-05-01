#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:36:23 2017

@author: Marianna K.
"""

import random
import string

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
    print("  ", len(wordlist), "words loaded.")
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

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise\
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    g_let = [] #the empty list in which we will put letters_guessed which are in secret_word
    secret_list = list(secret_word) #make list from string
    for char in secret_list:
        if char in letters_guessed:
            g_let.append(char)
    if len(secret_list) == len(g_let):
        return True
    else:
        return False



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    input_letter=input("Please, enter a letter (your guess)")
    return input_letter
    
    
    
number_of_guesses = 6
number_of_guessed_letters = 0
secret_word=choose_word(wordlist)
print("Hello! This is HANGMAAAAAN!!! Let's start! Good luck!\n")
print("You have a", str(number_of_guesses), "quesses. The secret word has", len(secret_word), "lowercase letters.")
#print(secret_word)
guessed_letters = []
letters_guessed = []

while number_of_guesses > 0 and number_of_guessed_letters < len(secret_word):
    input_letter = input("Please, enter a letter (your guess): ")
    letters_guessed.append(input_letter)
    if input_letter in secret_word:
        print("You'r lucky! The letter is in word!")
        guessed_letters+=input_letter
        
        for char in secret_word:
            
            if char in guessed_letters:
                print(char)                
            else:
                print("_")
        
    else:
        number_of_guesses -= 1
        print("Ooops! You have", str(number_of_guesses), "guesses")
    
    if number_of_guesses == 0:
            break
            
            
if get_guessed_word(secret_word, letters_guessed) == True:
    print("You win!")
else:
    print("Game over!")
    print("The word was", secret_word)


    
    


