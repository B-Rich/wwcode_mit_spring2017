# Problem Set 4A
# Name: Marianna Kovalova

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    n = len(sequence)
    s = list(sequence)
    list_of_permutations = []
    if n <= 1:
        return s
    else:
        for char in s:
            other = [other_char for other_char in s if other_char != char ]
            sublist_of_permutations = get_permutations(other)
            for i in sublist_of_permutations:
                list_of_permutations.append(char + i)
    return list_of_permutations   


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input0 = ''
    print('Input:', example_input0)
    print('Expected Output:', [])
    print('Actual Output:', get_permutations(example_input0))
    
    example_input1 = 'a'
    print('Input:', example_input1)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input1))
    
    example_input2 = 'ab'
    print('Input:', example_input2)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input2))
    
    example_input3 = 'abc'
    print('Input:', example_input3)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input3))