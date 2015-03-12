'''https://projecteuler.net/problem=49'''

from itertools import combinations

from utility import start, primes2

def p49():
    primes_list = primes2.PrimeList()
    primes_list.sieve(10000)
    
    # Group together all primes in the same permutation group
    permutations = {}
    for prime in primes_list.get_primes_in(range(1000, 10000)):
        prime_sorted_digits = tuple(sorted(str(prime)))
        if prime_sorted_digits in permutations:
            permutations[prime_sorted_digits].append(prime)
        else:
            permutations[prime_sorted_digits] = [prime]
    
    # Keep only those with at least three primes
    permutations = {sorted_digits: primes for sorted_digits, primes in
                    permutations.items() if len(primes) >= 3}
    
    # Get arithmetic sequences of length 3
    progressives = []
    for primes in permutations.values():
        # Pick all prime triplets
        for combo in combinations(primes, 3):
            #Check for progression
            if combo[2] - combo[1] == combo[1] - combo[0]:
                progressives.append(combo)
    
    #There should be two sequences
    assert len(progressives) == 2
    # Remove known sequence
    progressives.remove((1487, 4817, 8147))
    
    the_seq = progressives[0]
    return ''.join(str(prime) for prime in the_seq)

if __name__ == '__main__':
    start.time_functions(p49)
