'''
Created on 6 Dec 2010

@author: Qasim
'''

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math as maths

def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def p9():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = maths.sqrt(a**2 + b**2)
            if a+b+c == 1000 and is_pythagorean_triple(a, b, c):
                return(a, b, c, "-Product:", a*b*c)

def p9alt():
    """Using better boundaries"""
    for a in range(1, 334):
        # a <= b <= c
        for b in range(a, maths.ceil((1000-a)/2)):
            
            if (a-1000)*(b-1000) == 500000:
                c = 1000 - a - b
                return(a, b, c, "-Product:", a*b*c)

def p9alt2():
    """
    Using factorisation of a = m^2 - n^2, b = 2mn, c = m^2+n^2, for m > n
    a+b+c = 2m(m+n) = 1000
    m(m+n)=500, find m and n
    """
    
    for n in range(1, 23):
        for m in range(n+1, 24):
            if m*(m+n) == 500:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                return(a, b, c, "Product", a*b*c)

import utility.start

if __name__ == '__main__':
    utility.start.time_functions(p9, p9alt, p9alt2)
    
    """import time
    start = time.time()
    print(p9())
    print("Time taken: ", (time.time()-start)*1000, "ms", sep="")
    start = time.time()
    print(p9alt())
    print("Time taken: ", (time.time()-start)*1000, "ms", sep="")"""