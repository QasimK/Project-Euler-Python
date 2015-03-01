''' https://projecteuler.net/problem=44

Since you want the difference to be minimised, just find all differences
until you have a pentagonal number. To ensure it is minimum, work in
increasing distance.
'''

from utility import start, integers, generic

def dif(n, iterable):
    '''Yield differences of n in the list.
    
    eg. 2 dif for [1, 2, 3, 4, 5] will return (1, 3), (2, 4) etc.'''
    
    for i, number in enumerate(iterable):
        yield (number, iterable[i+n])

def get_smallest_diffs(iterable):
    '''Yield p1, p2, subtraction_difference for smallest n-diffs in a list'''
    
    diff_generators = [] # [ dif(1, iterable), dif(2, iterable), ...]
    consider_nexts = [] # [ (p1, p2), (q1, q2), ... ]
    diffs_list = [] #[ 1-diff (p2-p1), 2-diff, ...]
    
    def add_next_gen():
        next_index = len(diff_generators)
        new_generator = dif(next_index + 1, iterable)
        diff_generators.append(new_generator)
        update(next_index)
    
    def update(i):
        #Update index i in consider_nexts
        generator = diff_generators[i]
        pair = next(generator)
        diff = pair[1] - pair[0]
        try:
            consider_nexts[i] = pair[0], pair[1]
            diffs_list[i] = diff
        except IndexError:
            consider_nexts.append((pair[0], pair[1]))
            diffs_list.append(diff)
    
    add_next_gen()
    
    while True:
        smallest_diff = min(diffs_list)
        index_smallest = diffs_list.index(smallest_diff)
        pair = consider_nexts[index_smallest]
        
        # If smallest_diff is in last generator, add in next generator
        if index_smallest == len(diffs_list) - 1:
            add_next_gen()
        
        update(index_smallest)
        yield pair[0], pair[1], smallest_diff


def p44():
    pentagonals = generic.Sliceable(integers.get_pentagonals(),
                                    generic.Sliceable.less_than_last)
    
    for p1, p2, sub_dif in get_smallest_diffs(pentagonals):
        if sub_dif in pentagonals and p1 + p2 in pentagonals:
            return sub_dif


if __name__ == '__main__':
    start.time_functions(p44)
