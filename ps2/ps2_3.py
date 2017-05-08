# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:32:02 2017

@author: Marianna
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
    g_let = [] #the empty list in which we will put letters_guessed which are in secret_word
    secret_list = list(secret_word) #make list from string
    for char in secret_list:
        if char in letters_guessed:
            g_let.append(char) #make list with guessed letters
    if len(secret_list) == len(g_let):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
    represents which letters in secret_word have been guessed so far.
    '''
    part_secret_word = ''.join([char if char in letters_guessed else ' _ ' for char in secret_word]) # secret_word with '_'
    return part_secret_word
                              


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which
    letters have not
    yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase[:])
    '''
    The lowercase letters'abcdefghijklmnopqrstuvwxyz'
    '''
    available_letters = all_letters[:] #Make copy of all_letters
    for char in letters_guessed:
        available_letters.remove(char)
    return ''.join(available_letters)

#def letters_guessed():



def warnings_remaining(warnings, number_of_guesses):
    if warnings > 0:
        warnings -= 1
        print("You have", str(warnings), "warnings left.")
        return (warnings, number_of_guesses)
    elif warnings == 0:
        warnings = 0
        number_of_guesses -= 1
        print("You have 0 warnings left, so you lost 1 guess")          
        return (warnings, number_of_guesses)
    

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
number_of_guesses = 6
warnings = 3
number_of_guessed_letters = 0
secret_word = choose_word(wordlist)
print("Welcome to the game Hangman!")
print("You have", str(warnings), "warnings left.")
print("I am thinking of a word that is", len(secret_word), "letters long.")
print("--------------------------------")
letters_guessed = []

while number_of_guesses > 0:
    print("You have", str(number_of_guesses), "guesses left.")
    print("Available letters:: ", get_available_letters(letters_guessed))
    print("Secret word: ", get_guessed_word(secret_word, letters_guessed))
    guess = input("Please guess a letter: ")
    input_letter = str.lower(guess)
    if len(input_letter) == 1:
        if str.isalpha(input_letter) is True:
            if input_letter not in letters_guessed:
                letters_guessed.append(input_letter)
                if input_letter in secret_word:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                    print("--------------------------------")
                else:
                    number_of_guesses -= 1
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    print("--------------------------------")
            else:
                print("You've already tried this letter, choose another")
                (warnings, number_of_guesses) = warnings_remaining(warnings, number_of_guesses)
        elif str.isalpha(input_letter) is False:
            print("Oops! That is not a valid letter.")
            (warnings, number_of_guesses) = warnings_remaining(warnings, number_of_guesses)
    elif len(input_letter) > 1:
         print("Please, only one character at a time")
         (warnings, number_of_guesses) = warnings_remaining(warnings, number_of_guesses)
        
    if number_of_guesses == 0:
        print("Game over!")
        print("The word was", secret_word)
        break
    elif is_word_guessed(secret_word, letters_guessed) is True:
        print("You won!")
        break

