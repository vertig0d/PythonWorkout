'''Write a function, firstlast, that takes a sequence (string, list, or tuple) 
and returns the first and last elements of that sequence, in a two-element sequence of the same type. 
So firstlast('abc') will return the string ac, while firstlast([1,2,3,4]) will return the list [1,4].'''

def first_last(seq):
    if type(seq) not in (str, list, tuple):
        raise TypeError('Input Seq is of invalid data type')
    return seq[:1] + seq[-1:]

