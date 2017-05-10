# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:50:08 2017

@author: Marianna
"""
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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
      False otherwise
    '''
    g_let = [] # the empty list in which we will put letters_guessed which are in secret_word
    secret_list = list(secret_word) # make list from string
    for char in secret_list:
        if char in letters_guessed:
            g_let.append(char) # make list with guessed letters
    if len(secret_list) == len(g_let):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    part_secret_word = ''.join([char if char in letters_guessed else ' _ ' for char in secret_word]) # secret_word with '_'
    return part_secret_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase[:])
    '''
    The lowercase letters'abcdefghijklmnopqrstuvwxyz'
    '''
    available_letters = all_letters[:] # Make copy of all_letters
    for char in letters_guessed:
        available_letters.remove(char)
    return ''.join(available_letters)
    
    
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word(i) == other_word(i):
            return True
        else:
            return False


def warnings_remaining (warnings, number_of_guesses):
    '''
    The number of warnings the user has left.
    '''     
    if warnings > 0:
        warnings -= 1
        print("You have", str(warnings), "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("\n--------------------------------\n")
        return warnings, number_of_guesses
    elif warnings == 0:
        warnings = 0
        number_of_guesses -= 1
        print("You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))          
        print("\n--------------------------------\n")
        return warnings, number_of_guesses
    


def guesses_remaining (number_of_guesses, vowels, input_letter):
    '''
    The number of guesses the user has left
    '''
    if input_letter in vowels:
       number_of_guesses -= 2
    else:   
        number_of_guesses -= 1
    return number_of_guesses
        
                

def score (secret_word, number_of_guesses):
    '''
    Compute Total score
    '''
    unique_letters = []
    for char in secret_word:
        if char not in unique_letters:
            unique_letters.append(char)
    number_unique_letters = len(unique_letters)
    total_score = number_of_guesses * number_unique_letters
    return total_score


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)