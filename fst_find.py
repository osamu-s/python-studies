#!/usr/bin/env python

import itertools

def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item
    for which pred(item) is true.

    """
    # first_true([a,b,c], x) --> a or b or c or x
    # first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
    return next(itertools.ifilter(pred, iterable), default)

if __name__ == '__main__':
    print(first_true([1,2,3], 4))
    print(first_true([1,2,3], 4, lambda x: x>2))
    
    a = [4,0,1,2,3]
    senti = (len(a), len(a)+1)
    print((first_true(enumerate(sorted(a)), senti, lambda x: x[0] < x[1]))[0])
    
    d = { 'asd': { 'fst': 1, 'snd': 2},
          'qwe': { 'fst': 5, 'snd': 6} }
    print(first_true(d.values(), None, lambda x: x.get('snd', None) == 2))
