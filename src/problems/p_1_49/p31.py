'''
Created on 22 Sep 2011

@author: Qasim
'''

"""
Problem:
In England the currency is made up of pound, £, and pence, p, and
there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?
"""

"""Thoughts:
Need faster way to do it.
"""

import functools

import utility.start as start

ctable = [200, 100, 50, 20, 10, 5, 2, 1][::-1] #Faster for some reason.

def remove_dups(list_):
    """Remove duplicates from a list"""
    
    if len(list_) > 1:
        list_.sort()
        n = len(list_)
        last = list_[0]
        lasti = i = 1
        while i < n:
            if list_[i] != last:
                list_[lasti] = last = list_[i]
                lasti += 1
            i += 1
        return list_[:lasti]
    
    return list_


@functools.lru_cache(maxsize=None)
def form(value, max_denom):
    """Return a list of all possibilities which form value using
    the maximum denomination specified."""
    
    possibles = []
    
    for first_coin in [c for c in ctable if c <= max_denom]:
        remaining_value = value - first_coin
        if remaining_value < 0:
            break
        if remaining_value != 0:
            new_max_denom = min(max_denom, remaining_value, first_coin)
            for new_max_denom in [c for c in ctable if c <= new_max_denom]:
                new_possibles = form(remaining_value, new_max_denom)
                for new_possible in new_possibles:
                    addto = [first_coin]
                    addto.extend(new_possible)
                    addto.sort(reverse=True)
                    possibles.append(addto)
        else:
            possibles.append([first_coin])
    
    possibles = remove_dups(possibles)
    
    return possibles
    

def p31():
    possibilities = form(200, 200)
    #for p in possibilities:
    #    print(p)
    print(form.cache_info())
    return len(possibilities)
    

if __name__ == '__main__':
    start.time_functions(p31, profile=True)
