'''
Created on 11 Nov 2011

@author: Qasim
'''

"""Problem:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

"""Thoughts:
In digit notation ab/cd.
ab < cd => ab/cd < 1

a, c E [1, 9]
b, d E [0, 9]

Want:
1) a=c or a=d or b=c or b=d
AND 2) ab/cd = (i)b/d, (ii)b/c, (iii)a/d, (iv)a/c respectively
"""

def get_numerators(c, d):
    """For ab/cd, Return a, b such that ab < cd"""
    a = c
    b = d-1
    while b >= 0:
        yield a, b
        b -= 1
    
    a = c-1
    while a >= 1:
        b = 9
        while b >= 0:
            yield a, b
            b -= 1
        a -= 1

def generate_fractions():
    """Return all possible a, b, c, d combos where ab<cd
    
    AND when one digit on each side are the same
    (Both digits are never the same)"""
    for c in range(1, 10):
        for d in range(0, 10):
            for a, b in get_numerators(c, d):
                if a == c or a==d or b==c or b==d:
                    #Note two digits may be the same in the opposite order
                    #Thus implies 1 but that is impossible
                    if not(a==d and b==c):
                        yield a, b, c, d

def p33():
    for a, b, c, d in generate_fractions():
        numer = (10*a + b)
        denom = (10*c + d)
        fraction = numer/denom
        print(numer, denom)
        #Check for cancelling cases and whether if after cancelling you
        #have the same fraction
                
                

if __name__ == '__main__':
    import utility.start as start
    start.time_functions(p33)
