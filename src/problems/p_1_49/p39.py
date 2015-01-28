'''
Created on 28 Jan 2012

@author: Qasim
'''

"""Problem:
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

"""Thoughts:
Was done on paper.
"""

import math as m

def p39():
    py_triples = {}
    for p in range(12, 1001, 2):
        max_a = m.ceil((p/3) - 1)
        for a in range(3, max_a+1):
            max_b = m.ceil( (p-a)/2 - 1 )
            min_b = a+1
            for b in range(min_b, max_b+1):
                c = p-a-b
                
                lhs = a**2 + b**2
                rhs = c**2 
                if lhs-rhs == 0:
                    if p not in py_triples:
                        py_triples[p] = []
                    py_triples[p].append((a,b))
    
    the_p = 0
    max_l = 0
    for perimeter, solns in py_triples.items():
        current_l = len(solns)
        if current_l > max_l:
            the_p = perimeter
            max_l = current_l
    return the_p
        

def p39b():
    py_triples = {}
    for p in range(12, 1001, 2):
        max_a = m.ceil((p/3) - 1)
        for a in range(3, max_a+1):
            b = p*(2*a - p)/(2*(a - p)) #Must be whole number
            print(p, a, b, p-a-b)
            if m.floor(b) == m.ceil(b):
                #We have a triple
                if p not in py_triples:
                    py_triples[p] = []
                py_triples[p].append((a, b))
    
    the_p = 0
    max_l = 0
    for perimeter, solns in py_triples.items():
        current_l = len(solns)
        if current_l > max_l:
            the_p = perimeter
            max_l = current_l
    return the_p

if __name__ == '__main__':
    import utility.start as start
    start.time_functions(p39b)
