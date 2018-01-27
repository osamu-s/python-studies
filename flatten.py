#!/usr/bin/env python3
from itertools import chain
from collections import MutableSequence

# def flatten(lst):
#     if lst:
#         car, *cdr=lst
#         # car = lst[0]
#         # cdr = lst[1:]
#         if isinstance(car, (list,tuple)):
#             if cdr:
#                 return flatten(car) + flatten(cdr)
#             return flatten(car)
#         if cdr: 
#             return [car] + flatten(cdr)
#         return [car]

# def flatten(lst):
#     if lst:
#         car, *cdr=lst
#         return ((flatten(car) if isinstance(car, (list,tuple)) else [car]) 
#                 + flatten(cdr) )
#     else:
#         return []

# def flatten(lst):
#     return list(chain.from_iterable(
#         [ (flatten(l) if isinstance(l, (list,tuple)) else [l])
#           for l in lst ] ))

def flatten(lst, levels=None):
    def _core(lst, f):
        return chain.from_iterable(
            (f(l) if isinstance(l, MutableSequence) else [l]
             for l in lst
             if l not in  (None, 'None', 'null') ))

    def _wrapper1(lst):
        return _core(lst, _wrapper1)

    def _wrapper2(lst, levels):
        return (lst if levels <= 0
                else _core(lst, lambda x: _wrapper2(x, levels -1)) )

    return list(_wrapper1(lst) if levels == None
                else _wrapper2(lst, levels) )


def simple_flatten(lst):
    return list(chain.from_iterable(lst))


if __name__ == '__main__':
    test_data1 = [1, 2, [3, [4, [5]], 6], 7]
    print (flatten(test_data1))
    print (flatten(test_data1, levels=1))
    print (flatten(test_data1, levels=2))
    print (flatten([[1,[]], [[[2], 3], None], [[4]]], levels=2))
