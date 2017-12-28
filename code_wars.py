'''
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.
'''
from collections import Counter
import operator

def find_uniq(arr):
    '''
    INPUT:
        Array of string as a list

    OUTPUT:
        The string that is not similar to the all the other strings in the Array

    EXAMPLE:
        find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
        find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

    '''
    temp = []
    for item in arr:
        aa = (set(item.strip().lower()))
        temp.append(''.join(sorted(list(aa))))

    bb = Counter(temp)
    sorted_bb = sorted(bb.items(), key=operator.itemgetter(1))
    idx = temp.index(sorted_bb[0][0])
    return arr[idx]
