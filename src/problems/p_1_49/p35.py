"""
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

"""
If the number contains a "0" then one of the rotations will not be a prime.
    Consider the number abcdef...
    The rotations are abcdef..., bcdef..., cdef... and so on until each letter
    is at the end of the number
Therefore we can skip all numbers which contain the digit 0, 2, 4, 6, or 8.

Not Implemented:
If the number of n digits starts with a certain number, eg. 1 are done
then you can skip all other n-digit numbers which contain 1.
    eg 100 - 199 is completed (1xx), this means you can skip x1x, xx1
"""

import utility.primes2 as primes
import utility.integers as integers

def p35():
    prime_list = primes.PrimeList()
    prime_list.sieve(1000000)
    
    number = 1 #NOTE: 2 is blocked out by (***)
    for prime in prime_list.get_primes():
        if prime >= 10**6:
            break
        
        #(***)
        if any(x in str(prime) for x in ["0", "2" ,"4", "6", "8"]):
            continue
        
        for rotation in integers.get_rotations(prime):
            if not prime_list.is_prime(rotation):
                break
        else:
            #Did not break => They are all prime
            number += 1
    return number


if __name__ == '__main__':
    import utility.start
    #import cProfile
    #cProfile.run('utility.start.time_functions(p35)')
    utility.start.time_functions(p35)
