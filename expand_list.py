#!/usr/bin/env python

import json

def expand_dict(data, list_key, new_key=None):
    def _update(dsrc, udata):
        dsrc.update(udata)
        return dsrc

    if not isinstance(data, dict):
        raise TypeError("Item is not a valid dict")
        
    wk_data = dict(data)                       # preserve original data
    list_data = wk_data.pop(list_key)
    if not isinstance(list_data, list):
        msg = 'value: {} derived by {} is not a list'.format(list_data, list_key)
        raise TypeError(msg)
    key = new_key if new_key else list_key
    return [ _update(dict(wk_data), {key: val}) for val in list_data ]


def main():
    testdict = {
        'item1': 'val1',
        'item2': 'val2',
        'list_item': [ 'foo', 'bar', 'baz' ]
    }
    print(json.dumps(expand_dict(testdict, 'list_item', 'item3'),
                     indent=2))
        

if __name__ == '__main__':
    main()
