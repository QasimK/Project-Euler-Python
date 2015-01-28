'''
Created on 6 Dec 2010

@author: Qasim
'''

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

'''
1 digit: None
2 digits: If 1+ of a, b >= 5 then No more solutions
3 digits: If 1+ of a, b >= 7 then No more solutions
4 digits: If 1+ of a, b >= 8 then No more solutions
5 digits: If 1+ of a, b >= 9 then No more solutions

7 digits: 2,540,160 is Largest possible curious number
(7 x 9! = 2,540,160)

Also we note that the factorials are even except for 0! = 1! = 1
Therefore we don't need to check odd numbers unless they have an odd number
of 0s and 1s

'''

import utility.integers

def p34():
    list_of_curious_numbers = []
    for n in range (10, 2540161):
        if not n % 2: #odd
            str_n = str(n)
            if str_n.count("0") + str_n.count("1") % 2: #not an odd number of 0s and 1s
                continue
            
        if utility.integers.digit_factorial(n) == n:
            list_of_curious_numbers.append(n)
    
    return sum(list_of_curious_numbers)

def p34alt():
    """Find the digit_factorial for n digit numbers and then see if it is equal
    to any number that is n digits!"""
    
    pass

import utility.start

if __name__ == '__main__':
    utility.start.time_functions(p34)
