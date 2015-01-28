'''
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² − 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, starting
with n = 0.
'''

'''
a and b are odd.
But b is prime (from n = 0)
(3) Also when n=b, the result is not prime
'''

import utility.primes as primtest

def p27():
    _max = (0, 0, 0) #(a, b, prime-count)
    
    def enumerate_b(sign, _max):
        for b in primtest.get_primes():
            if b > 999:
                break
            
            b *= sign
            
            #(3)
            if b**2 < _max[2]**2:
                continue
            
            prime = True
            n = 0
            while prime:
                x = n**2 + a*n + b
                if primtest.is_prime(x):
                    n += 1
                else:
                    prime = False
                    if _max[2] < n:
                        _max = (a, b, n)
        
        return _max
    
    for a in range(-999, 1000, 2):
        _max = enumerate_b(1, _max)
        _max = enumerate_b(-1, _max)
    
    return _max[0]*_max[1]

if __name__ == '__main__':
    import time
    start = time.time()
    print(p27())
    print("Time taken: ", (time.time()-start)*1000, "ms", sep="")
