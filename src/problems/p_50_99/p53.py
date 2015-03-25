''' https://projecteuler.net/problem=53
(Note this has a corresponding solution document.)

We have symmetry with nCr, in that nCr = nC(n-r).
Thus we only check for r=n/2 rounded down.

Looking at Pascal's Triangle, on a particular row once we have the smallest r
such that nCr > 10e6, then we know the ranges of r for that particular n.

We also know this r will work for n+1 (from comparing nCr and (n+1)Cr), so work
from that r to smaller r.
'''

from utility import start, integers

def get_working_range(n, r):
    """Return all k s.t. nCk > X, given smallest r such that nCr > X"""
    return range(r, n - r + 1)
    

def p53():
    working_values = []
    # First ones that work from question
    n = 23
    r = 10
    
    while n <= 100:
        # We under-shoot the r value by 1:
        while integers.choose(n, r) >= 10**6:
            r -= 1
        
        # The last r that worked is actually r + 1:
        working_values.extend([(n, k) for k in get_working_range(n, r + 1)])
        
        n += 1
    
    return len(working_values)

if __name__ == '__main__':
    start.time_functions(p53)
