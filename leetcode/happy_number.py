'''

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
#%%
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    possible_sums = set()
    while True:
        n = sum([int(char)**2 for char in str(n)])
        if n == 1:
            return True
        if n in possible_sums:
            return False
        possible_sums.add(n)


#%%
isHappy(19)

#%%
'''
This was the original and i was able to condense
it after seeing other examples
    s = str(n)
    happy = False

    while not happy:
        square_of_digits = []
        for char in s:
            square_of_digits.append(int(char)**2)
        if sum(square_of_digits) == 1:
            return True
        s = str(sum(square_of_digits))
        print(s)
        #else infinite loop
        count += 1
        if count == 100:
            break
        '''