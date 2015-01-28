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
