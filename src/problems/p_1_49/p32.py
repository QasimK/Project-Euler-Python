'''
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

'''
The #digits in the product >= #digits of multiplicand + #digits of multiplier
eg. 100x100 >= 10,000 means 3+3 = 6-1 = 5

Similarly the maximum #digits in product is the above minimum plus one.
eg. 100x100 = 10,000, but 999x999 <= 999,999

So the product is either 4 or 5 digits.

This leaves only 7 split locations in: 1 [1], 2, 3, 4, 5, 6, 7, 8 [8] 9:
(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)

But 10x10 and 99x99 are not possible so: actually (1, 4) does not work,
(2, 4) does not work and (3, 4) does not work.

So the product is 4 digits exactly.

So we have the split locations: (1, 5), (2, 5) and (3, 5).
ie. 1 digit x 4 digit, 2 digit x 3 digit and 3 digit x 2 digit.
ie. two distinct possibilities: 1 digit x 4 digit and 2 digit x 3 digit.
'''

import itertools

import utility.start as start

def p32():
    valid_products = set()
    
    for k in (1, 2):
        base = '123456789'
        for m1 in itertools.permutations(base, k):
            remaining = base
            for l in m1:
                remaining = remaining.replace(l, '')
            m1 = int(''.join(m1))
            
            for m2 in itertools.permutations(remaining, 5-k):
                remaining2 = remaining
                for l in m2:
                    remaining2 = remaining2.replace(l, '')
                m2 = int(''.join(m2))
                
                p = m1 * m2
                if sorted(str(p)) == list(remaining2):
                    valid_products.add(p)
    
    return sum(valid_products)


if __name__ == '__main__':
    start.time_functions(p32)
