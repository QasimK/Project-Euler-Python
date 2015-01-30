''' https://projecteuler.net/problem=41

Assuming n can be 9 maximum.
n cannot be 9 because sum of 1, ..., 9 is 45 and thus divisible by 9.
n cannot be 8 because sum of 1, ..., 8 is 36 and thus divisible by 9.
Thus I am assuming n is 7.
'''

from utility import start, primes2, generic

def p41():
    MAX_NUM = 7654321
    prime_list = primes2.PrimeList()
    prime_list.sieve(MAX_NUM)
    
    max_prime_pandigital = 0
    for prime in prime_list.get_primes_grange(generic.grange(MAX_NUM, -1)):
        if ''.join(sorted(str(prime))) == '1234567':
            max_prime_pandigital = prime
            break
    
    return max_prime_pandigital

if __name__ == '__main__':
    start.time_functions(p41)