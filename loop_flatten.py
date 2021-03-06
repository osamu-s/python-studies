#!/usr/bin/env python3
from collections import MutableSequence

def flatten(mylist, levels=None):
    def _core(ls, levels):
        if levels is not None:
            levels = int(levels) -1
        for element in ls:
            if element in (None, 'None', 'null'):
                # ignore undefined items
                continue
            elif (isinstance(element, MutableSequence) and
                  (levels is None or levels >= 0) ):
                    _core(element, levels)
            else:
                ret.append(element)
        return

    ret = []
    _core(mylist, levels)
    return ret

if __name__ == '__main__':
    print (flatten([1, [2, 3], 4]))
    print (flatten([[1,2], [2, 3], [[4]]], levels=1))
    # nil break example: expected [1, 2, 3, 4] but [1]
    print (flatten([1, None, [2, 3], 4]))
    print (flatten([1, [], [2, 3], 4]))
    # flatten level error example
    print (flatten([[1,2], [2, 3], [[4]]], levels=1))
