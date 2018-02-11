#!/usr/bin/env python3
from collections import MutableSequence

def flatten(mylist, levels=None):

    ret = []
    for element in mylist:
        if element in (None, 'None', 'null'):
            # ignore undefined items
            break
        elif isinstance(element, MutableSequence):
            if levels is None:
                ret.extend(flatten(element))
            elif levels >= 1:
                levels = int(levels) - 1
                ret.extend(flatten(element, levels=levels))
            else:
                ret.append(element)
        else:
            ret.append(element)

    return ret

if __name__ == '__main__':
        
    print (flatten([1, [2, 3], 4]))
    print (flatten([[1,2], [2, 3], [[4]]], levels=1))
    # nil break example: expected [1, 2, 3, 4] but [1]
    print (flatten([1, None, [2, 3], 4]))
    print (flatten([1, [], [2, 3], 4]))
    # flatten level error example
    print (flatten([[1,2], [2, 3], [[4]]], levels=1))

