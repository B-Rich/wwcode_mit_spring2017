# Problem Set 4B
# Name: Marianna Kovalova

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = wordlist

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.message_text

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        alphabet_lowercase = string.ascii_lowercase
        alphabet_uppercase = string.ascii_uppercase
        encryption_dict = {
                letter:alphabet_lowercase[(alphabet_lowercase.index(letter)+shift) % 26]
            for letter in alphabet_lowercase}
        encryption_dict_upper = {
                letter:alphabet_uppercase[(alphabet_uppercase.index(letter)+shift) % 26]
            for letter in alphabet_uppercase}
        encryption_dict.update(encryption_dict_upper)
        return encryption_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        encryption_dict = self.build_shift_dict(shift)
        message_text_encrypted = "".join([encryption_dict.get(letter)
        if letter in encryption_dict else letter for letter in self.message_text])
        return message_text_encrypted

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self, shift)
        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = CiphertextMessage.get_message_text(self)
        self.valid_words = self.get_valid_words()

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        shifts = []
        temp_text = self.message_text
        for shift in range (26):
            temp_text = self.message_text
            temp_text = self.apply_shift(shift)
            chars = " ,!@#$%^&*()-_+={}[]|\:;'<>?./\""
            for c in chars:
                temp_text = temp_text.replace(c, ' ')
            temp_text = temp_text.split()
            for word in temp_text:
                count = 0                        
                if is_word(self.valid_words, word) is True:
                    count += 1
            shifts.append(count)
        best_shift = shifts.index(max(shifts))
        decrypted_message = self.apply_shift(best_shift)
        return (best_shift, decrypted_message)

if __name__ == '__main__':
    
    wordlist = load_words(WORDLIST_FILENAME)

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('Hello, world!', 2)
#    print('Expected Output: Jgnnq, yqtnf!')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#    print("-------------------------------------------------------")
#    
#    plaintext = PlaintextMessage('Although never is often better than *right* now.', 4)
#    print('Expected Output: Epxlsykl riziv mw sjxir fixxiv xler *vmklx* rsa.')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#    print("-------------------------------------------------------")
#    
#    plaintext = PlaintextMessage("Namespaces are one honking great idea -- let's do more of those!", 25)
#    print("Expected Output: Mzldrozbdr zqd nmd gnmjhmf fqdzs hcdz -- kds'r cn lnqd ne sgnrd!")
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#    print("-------------------------------------------------------")
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('Jgnnq, yqtnf!')
#    print('Expected Output:', (24, 'Hello, world!'))
#    print('Actual Output:', ciphertext.decrypt_message())
#    print("-------------------------------------------------------")
#    
#    ciphertext = CiphertextMessage('Epxlsykl riziv mw sjxir fixxiv xler *vmklx* rsa.')
#    print('Expected Output:', (22, 'Although never is often better than *right* now.'))
#    print('Actual Output:', ciphertext.decrypt_message())
#    print("-------------------------------------------------------")
#    
#    ciphertext = CiphertextMessage("Mzldrozbdr zqd nmd gnmjhmf fqdzs hcdz -- kds'r cn lnqd ne sgnrd!")
#    print('Expected Output:', (1, "Namespaces are one honking great idea -- let's do more of those!"))
#    print('Actual Output:', ciphertext.decrypt_message())
#    print("-------------------------------------------------------")

    ciphertext = CiphertextMessage(get_story_string())
    print("The appropriate shift value and unencrypted story is: ", ciphertext.decrypt_message())