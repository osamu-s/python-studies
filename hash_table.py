#!/usr/bin/env python

import json
from collections import defaultdict, Mapping, Iterable
from functools import reduce

def hash_table(data, key_item):
    """ Make Hash table by given key's value.
        - Hash function: by native python hash
        - Collision resolution: Separate chaining with lists by python list

        list_object = [
            {'key_a': 'val_1a', 'key_b': 'val_1b', ...},
            {'key_a': 'val_2a', 'key_b': 'val_2b', ...},
            {'key_a': 'val_3a', 'key_b': 'val_3b', ...},
            {...},
        ]

        hash_table(list_object, 'key_b') = {
            val_1b: [{'key_a': 'val_1a', 'key_b': 'val_1b', ...}],
            val_2b: [{'key_a': 'val_2a', 'key_b': 'val_2b', ...}],
            val_3b: [{'key_a': 'val_3a', 'key_b': 'val_3b', ...}],
            ...
        }

        :param list_object: list of dictionaries
        :returns: a dictionary of 'index key':'dict body'
    """
    def update_ht(ht, list_item):
        if not isinstance(list_item, Mapping):
            raise TypeError("List item is not a valid dict")
        try:
            # cause KeyError if dict does not contain key_item.
            key = list_item[key_item]
            # cause TypeError if key is not hashable.
            _ = hash(key)
        except TypeError:
            msg = 'key: {} derived by {} is not hashable'.format(key, key_item)
            raise TypeError(msg)
        except:
            raise

        ht[key].append(list_item)
        return (ht)

    # Check if data is valid
    if not isinstance(data, (Mapping, Iterable)):
        raise TypeError("Type is not a valid list, set, or dict")

    list_object = (data.values() if isinstance(data, Mapping)
                   else data )
    return reduce(update_ht, list_object, defaultdict(list))

def main():
    testlist=[{ 'name': 'k1-c27-14-sv',
                'val': 4 },
              { 'name': 'k1-c27-13-sv',
                'val': 9 },
              { 'name': 'k1-c27-13-sv',
                'val': 12 },
              { 'name': 'k1-c27-12-sv',
                'val': 9 }
    ]
    testdict={
        'item1': { 'name': 'k1-c27-14-sv',
                   'val': 4 },
        'item2': { 'name': 'k1-c27-13-sv',
                   'val': 9 },
        'item3': { 'name': 'k1-c27-13-sv',
                   'val': 12 },
        'item4': { 'name': 'k1-c27-12-sv',
                   'val': 9 }
    }

    print (json.dumps(hash_table(testlist, 'name'), indent=2))
    print (json.dumps(hash_table(testdict, 'val'), indent=2))

if __name__ == '__main__':
    main()
