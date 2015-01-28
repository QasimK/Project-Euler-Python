"""Problem:
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Answer: 748317
"""

"""Thoughts:
Note 379 is not a truncatable prime even though it is from 3797.
"""

import utility.primes2 as p33

pl = p33.PrimeList()

def get_truncates(prime):
    #Remove from right
    str_prime = str(prime)
    if not pl.is_prime(int(str_prime[-1]))\
    or not pl.is_prime(int(str_prime[0])):
        return None
    
    truncated_primes = []
    #Truncate from right first
    for i in range(1, len(str_prime)-1):
        new_prime = int(str_prime[:-i])
        if not pl.is_prime(new_prime):
            break
        else:
            truncated_primes.append(new_prime)
    else:
        #Did not break, truncate from left
        for i in range(1, len(str_prime)):
            new_prime = int(str_prime[i:])
            if not pl.is_prime(new_prime):
                break
            else:
                truncated_primes.append(new_prime)
        else:
            return truncated_primes
    
    return None

def p37a():
    real_answer = []
    
    pg = pl.get_primes(10)
    prime = 2
    
    while prime < 10**6:
        prime = next(pg)
        truns = get_truncates(prime)
        if truns:
            real_answer.append(prime)
            if len(real_answer) == 11:
                break
    
    return sum(real_answer)


if __name__ == '__main__':
    import utility.start as start
    start.time_functions(p37a)
