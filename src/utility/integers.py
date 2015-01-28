'''
Created on 17 Jul 2010

@author: Corsair
'''

import math as maths

def is_integer(number):
    """Return if number is an integer"""
    return int(number) == number


def digit_factorial(number):
    """Return the sum of the factorial of the digits of the number
    
    eg. 245! = 2! + 4! + 5!"""
    
    total = sum(maths.factorial(int(digit)) for digit in str(number))
    return total


def get_rotations(number):
    """Return the unique rotations of a number
    
    Example(1234): 1234, 2341, 3412, 4123"""
    
    rotations = set([number])
    for rot_n in range(1, len(str(number))):
        rotation = str(number)
        for _ in range(1, rot_n + 1):
            rotation = rotation[1:] + rotation[0]
        rotations.add(int(rotation))
    return list(rotations)


def get_triangle_number(n):
    return 0.5*n*(n+1)

def get_triangle_numbers():
    """A generator yielding all triangle numbers (1, 3, 6, 10, 15, ...)
    
    Note: nth triangle number = 0.5n(n+1)"""
    triangle_number = 0
    i = 1
    while True:
        triangle_number += i
        i += 1
        yield triangle_number

def is_triangle_number(number):
    """This is rather slow as there is no caching
    
    Warning there may be precision issues with very large numbers"""
    
    return is_integer(maths.sqrt(2*number + 0.25) - 0.5)
    
    triangle_numbers = get_triangle_numbers()
    for triangle_number in triangle_numbers:
        if number == triangle_number:
            return True
        elif number < triangle_number:
            return False
