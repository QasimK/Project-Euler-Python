'''***Use primes2 instead.***'''

import math as maths

import utility.factors

checked_upto = 3 #Including this number
list_of_prime_numbers = set([2, 3])

def sieve(upto):
    """Calculate the list of primes upto upto by using a sieve method"""
    non_primes = set()
    for check_number in range(2, maths.floor(upto/2) + 1):
        x = 2
        non_prime = check_number*x
        while non_prime <= upto:
            non_primes.add(non_prime)
            x += 1
            non_prime = check_number*x
    return non_primes


def is_prime(number):
    """ Is the positive integer, number, a prime number? """
    global checked_upto, list_of_prime_numbers
    
    def continue_checking():
        global checked_upto, list_of_prime_numbers
        
        #If we are at an even number, we must go to an odd one (for ***)
        if checked_upto % 2 == 0:
            checked_upto -= 1 #(see ***)
        
        while checked_upto < number:
            #We will always be at odd numbers
            checked_upto += 2 #(***)
            
            factor_limit = maths.floor(maths.sqrt(checked_upto))
            #Do not need to check past the square root for factors
            
            #Only prime factors need to be checked against
            #(p for p in list_of_prime_numbers if p <= factor_limit):
            #BUT this expression is slower than range!
            for possible_factor in range(3, factor_limit+1, 2):
                if utility.factors.is_factor(possible_factor, checked_upto):
                    break #The number is not a prime
            else:
                #Did not break (the number is a prime)
                list_of_prime_numbers.add(checked_upto)
    
    def get_from_list():
        if number % 2 == 0:
            return False
        
        is_it_prime = number in list_of_prime_numbers
        return is_it_prime
    
    if number == 2:
        return True
    elif number <= checked_upto:
        #Is the number prime? Is it in the existing list of prime numbers?
        return get_from_list()
    else:
        continue_checking()
        #No looping should occur
        return is_prime(number)

def get_primes():
    yield 2
    yield 3
    count = 3
    while True:
        count += 2
        if is_prime(count):
            yield count