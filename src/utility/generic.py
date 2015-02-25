def grange(start=1, step=1, stop=None):
    """Generalised version of range() - could be infinite
    
    Note the difference in the order of arguments from those of range()."""
    
    if stop is None:
        x = int(start)
        dif = int(step)
        while True:
            yield x
            x += dif
    else:
        for x in range(start, stop, step):
            yield x


class Sliceable(list):
    """Make a general iterable (e.g. a generator) subscriptable like a list.
    
    contains_check(item, current_list) is a function that returns:
        True: return whether the item is in the list
        False: continue populating the list
    This is called continually to populate the list, so you must return True
    at some point."""
    
    def __init__(self, iterable, contains_check):
        super().__init__()
        self.iterable = iterable
        self.contains_check = contains_check
    
    def __iter__(self):
        k = 0
        while True:
            yield self[k]
            k += 1
    
    def __getitem__(self, key):
        try:
            max_index = key.stop
        except AttributeError:
            max_index = key
        
        while len(self) <= max_index:
            self.append(next(self.iterable))
        
        return list.__getitem__(self, key)
    
    def __contains__(self, item):
        while True:
            if self.contains_check(item, self):
                return super().__contains__(item)
            else:
                self.append(next(self.iterable))
    
    @staticmethod
    def less_than_last(item, current_list):
        """contains_check: Return whether item is less than last list's item"""
        try:
            return item < current_list[-1]
        except IndexError:
            return False
