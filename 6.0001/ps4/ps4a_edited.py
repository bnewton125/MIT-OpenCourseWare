# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    def permute(seq, perm):
        if len(seq) < 1:  # Out of letters to permute so stop recursion
            return
        else:  # still have letters to permute through so continue recursion
            if len(perm) == 0:  # basically a first letter check
                perm.append(seq[0])  # only permutation of the first letter are that letter
            else:  # for each different permutation fill
                perms_copy = perm.copy()  # create a copy of perms so perms can be emptied
                perm.clear()  # empty perms
                for word in perms_copy:  # for each existing word in perms fill out permutations into perms
                    for letters in range(len(word)+1):
                        if letters == 0:
                            perm.append(str(seq[0] + word))
                        elif letters == len(word)+1:
                            perm.append(str(word + seq[0]))
                        else:
                            perm.append(str(word[:letters] + seq[0] + word[letters:]))
            permute(seq[1:], perm)  # recurse with the first letter ripped out

    permutations = []
    permute(sequence, permutations)
    return permutations


if __name__ == '__main__':
    #EXAMPLE
    example_input = 'cba'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('')

    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', ['zyx', 'yzx', 'yxz', 'zxy', 'xzy', 'xyz'])
    print('Actual Output:', get_permutations(example_input))
    print('')

    example_input = 'mno'
    print('Input:', example_input)
    print('Expected Output:', ['onm', 'nom', 'nmo', 'omn', 'mon', 'mno'])
    print('Actual Output:', get_permutations(example_input))