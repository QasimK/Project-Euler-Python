''' https://projecteuler.net/problem=46

odd = prime + 2*Square
odd = 2 + 2*square  ==> prime != 2

1, 3, 5, 7 are not composite; Problem checked up to 33.
Work up from 35, 37... and subtract 2*square and see if any is prime.

square starts from 1, because odd must be a composite.
square inclusively ends at math.floor(math.sqrt((odd - 3) / 2))
'''

import math

from utility import start, generic, primes2

def p46():
    primes = primes2.PrimeList()
    
    for odd in generic.grange(35, 2):
        if primes.is_prime(odd):
            continue
        for psquare in range(1, math.floor(math.sqrt((odd - 3) / 2)) + 1):
            square = 2 * psquare**2
            if primes.is_prime(odd - square):
                break
        else:
            return odd

if __name__ == '__main__':
    start.time_functions(p46)
