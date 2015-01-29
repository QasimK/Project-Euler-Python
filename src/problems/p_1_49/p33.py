""" https://projecteuler.net/problem=33

In digit notation consider ab/cd, where 1 <= a, b, c, d, <= 9 and ab < cd.

Want:
(a) ab/cd = (i)b/d, or (ii)b/c, or (iii)a/d, or (iv)a/c
(b)   AND   (i)a=c, or (ii)a=d, or (iii)b=c, or (iv)b=d
"""

import fractions
from utility import start

def p33():
    the_fracs = []
    for denominator in range (11, 100):
        c = denominator // 10
        d = denominator % 10
        if d == 0:
            continue
        for numerator in range(11, denominator):
            a = numerator // 10
            b = numerator % 10
            if b == 0:
                continue
            
            frac = numerator/denominator
            if (a == c and frac == b/d) or (a == d and frac == b/c) or\
              (b==c and frac == a/d) or (b == d and frac == a/c):
                print((numerator, denominator))
                the_fracs.append(fractions.Fraction(numerator, denominator))
    
    final_frac = fractions.Fraction(1)
    for frac in the_fracs:
        final_frac *= frac
    return final_frac.denominator

if __name__ == '__main__':
    start.time_functions(p33)
