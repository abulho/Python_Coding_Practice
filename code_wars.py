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

#-----------------------------------------------------------------------------------------------------#
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
'''
import numpy as np
def solution(number):
    '''
    INPUT:
        number

    OUTPUT:
        The sum of all the number divisible by three and five.

    EXAMPLE:
        solution(10) --> 23
        passing number 10 into the function should return 23
    '''
    nums = np.array(range(1,number))
    mask3 = nums % 3 == 0
    mask5 = nums % 5 == 0
    nums3 = nums[mask3]
    nums5 = nums[mask5]
    return sum(list(set((np.append(nums3,nums5)))))
