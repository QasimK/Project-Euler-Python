import array
import math as maths

import utility.factors as factors
import utility.generic as ug

class PrimeList:
    """Generate and check for prime numbers"""
    
    def __init__(self):
        #: Starting from 0, 1, 2, 3, 4, 5, .... 1 means it *IS* a prime
        self.number_list = array.array('b', [0, 0, 1, 1, 0, 1])
    
    def max_known_number(self):
        """Return the maximum number which is known to be a prime or not"""
        return len(self.number_list)-1
    
    def is_prime(self, number):
        if self.max_known_number() < number:
            self.continue_checking(number)
        
        if self.number_list[number] == 1:
            return True
        else:
            return False
    
    def sieve(self, upto_num):
        """Generate primes upto and inc. the number specified.
        
        Requires a prime list holder to generate into."""
        max_cur_known = self.max_known_number()
        
        num_new = upto_num - max_cur_known
        #All new numbers are primes until they are crossed off
        self.number_list.extend(array.array('b', [1])*num_new)
        
        for marker_num in range(2, maths.floor(upto_num/2) + 1):
            #For efficiency only use prime marked numbers
            if not self.is_prime(marker_num):
                continue
            
            min_x = max(maths.floor(max_cur_known / marker_num) + 1, 2)
            max_x = maths.floor(upto_num / marker_num)
            non_primes = (marker_num*x for x in range(min_x, max_x+1))
            
            for non_prime in non_primes:
                self.number_list[non_prime] = 0
    
    def continue_checking(self, upto_num):
        """Continue building primes upto upto_num
        
        This is slower than using sieve"""
        checked_upto = self.max_known_number()
        #Only need to check odd numbers!
        if checked_upto % 2 == 0:
            checked_upto -= 1
        
        while checked_upto < upto_num:
            checked_upto += 2
            self.number_list.extend([0]) #Even number, (+1)
            #Now check the current odd number, (+2)
            
            factor_limit = maths.floor(maths.sqrt(checked_upto))
            for possible_factor in range(3, factor_limit+1, 2):
                if factors.is_factor(possible_factor, checked_upto):
                    self.number_list.extend([0])
                    break #The number is not a prime
            else:
                self.number_list.extend([1]) #Did not break => Prime
    
    def get_primes(self, startnum=2):
        """A generator which returns prime numbers
        
        It starts from 2 unless specified otherwise"""
        for i in ug.grange(startnum):
            if self.is_prime(i):
                yield i
    
    def get_primes_grange(self, grange):
        """Return generator yielding primes in generic.grange.
        
        If you have a large grange, you are better off doing a sieve first."""
        for i in grange:
            if self.is_prime(i):
                yield i
    
    def __str__(self):
        s=""
        for i, is_prime in enumerate(self.number_list):
            s += "%s: %s\n"%(i, ("Yes" if is_prime==1 else "No"))
        return s
    
    def _printraw(self):
        s=""
        for i, is_prime in enumerate(self.number_list):
            s += "%s: %s\n"%(i, is_prime)
        print(s)
