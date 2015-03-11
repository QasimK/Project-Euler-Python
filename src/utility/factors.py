import math as maths

def is_factor(possible_factor, number):
    """Is possible_factor a factor number?"""
    return number % possible_factor == 0


def get_factors(number):
    """Return all natural factors of number"""
    
    #Must be integer
    if int(number) != number:
        return None
    
    #No natural factors for 0 and -ve integers
    if number <= 0:
        return []
    
    #Special case as factors = [1, number] means factors = [1, 1]
    if number == 1:
        return [1]
    
    factors = [1, number]
    
    #Optimisation:
    #Odd numbers cannot have even factors (from p21)
    if number % 2 == 1:
        #Odd
        begin = 3
        step = 2
    else:
        begin = 2
        step = 1    
    
    go_upto = maths.floor(maths.sqrt(number))
    for possible_factor in range(begin, go_upto+1, step): #Excludes go_upto+1
        if is_factor(possible_factor, number):
            factors.append(possible_factor)
            other_factor = int(number/possible_factor)
            #Exclude corner case of square numbers
            if other_factor != possible_factor:
                factors.append(other_factor)
    
    return factors


def get_proper_divisors(number):
    """Return all proper divisors of a number (ie. all factors excluding number)
    
    Return [] for 1
    Return [] for 0, -1, -2, ..."""
    
    factors = get_factors(number)
    if factors == []:
        return []
    else:
        factors.remove(number)
        return factors


def get_proper_factors(number):
    """Get all factors of a number excluding 1 and the number"""
    factors = get_factors(number)
    try:
        factors.remove(1)
        factors.remove(number)
    except ValueError:
        pass
    return factors


def euclids_algorithm(a, b):
    """Yield (q, r, A, B) at each step of Euclid's extended algorithm"""
    A = [0, 1]
    B = [1, 0]
    r = None
    while r != 0:
        q = maths.floor(a/b)
        r = a - q*b
        Anext = q*A[-1] + A[-2]
        Bnext = q*B[-1] + B[-2]
        A.append(Anext)
        B.append(Bnext)
        yield q, r, Anext, Bnext
        a = b
        b = r


def get_euclids_table(a, b):
    """Get the entire table from Euclid's algorithm [(q, r, a, b), ...]"""
    return [(q, r, a, b) for q, r, a, b in euclids_algorithm(a, b)]


def get_hcf(a, b):
    """Return the highest common factor of two numbers"""
    #Uses Eulers algorithm
    return get_euclids_table(a, b)[-2][1]


def get_lowest_fraction(a, b):
    """Return the fraction a/b in its lowest terms (a', b')"""
    et = get_euclids_table(a, b)
    return et[-1][2], et[-1][3]
