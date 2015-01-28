'''
Created on 25 May 2010

@author: Qasim
'''

'''
A perfect number is a number for which the sum of its
proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is
a perfect number.

A number n is called deficient if the sum of its proper
divisors is less than n and it is called abundant if this
sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant
numbers is 24. By mathematical analysis, it can be shown that all
integers greater than 28123 can be written as the sum of two abundant
numbers. However, this upper limit cannot be reduced any further
by analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers.
'''

import utility.factors as factors

#Zegote number = A number which can be expressed as the sum of two abundants
#Antizegote = A number which CANNOT be expressed as the sum of two abundants

def get_all_abundants(max_number):
    """Return all abundant numbers upto but excluding max_number"""
    abundants = []
    #12 is known to be the smallest abundant
    for n in range(12, max_number):
        if sum(factors.get_proper_divisor(n)) > n:
            abundants.append(n)
    return abundants

def p23():
    '''
    I will find all Zegotes in [1, 28123] and remove them from the
    set {1, 2, ..., 28123}.
    
    The largest abundant number needed, x, is known to follow:
        x+12 = 28,123 (largest possible antizegote)
        therefore x = 28,111
    There is no need to check any abundants larger than this.
    Similarly, the smallest abundant = 12.
    '''
    
    abundants = get_all_abundants(28111+1)
    
    #Find all zegotes and remove them from {1, 2, ..., 28123}
    full_set = set([num for num in range(1, 28123+1)])
    zygote_set = set()
    for i, first_number in enumerate(abundants):
        go_upto = 28123 - first_number
        for second_number in abundants[i:]:
            if second_number > go_upto:
                break
            
            zygote = first_number+second_number
            try:
                zygote_set.add(zygote)
            except ValueError:
                pass
    
    list_of_antizygotes = full_set - zygote_set
    return sum(list_of_antizygotes)

if __name__ == '__main__':
    #print(get_all_abundants(20))
    
    import time
    start = time.time()
    print(p23())
    print("Time taken: ", (time.time()-start)*1000, "ms", sep="")