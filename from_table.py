#!/usr/bin/env python

import json
import csv
from collections import OrderedDict

def table_transpose(table_list):
    return (list(ln) for ln in zip(*table_list))

def tokenize(tbl_str, ttype,
             frame=0,
             junction_char='+',
             separator=','):

    def pretty():
        sep_idxs = [ i for i, c in enumerate(tbl_ln[frame])
                     if c == junction_char ]
        slices = [ (s+1, e-1) for s, e in zip([0]+sep_idxs, sep_idxs)[1:]]
        return ([ln[s:e].strip() for s, e in slices]
                for ln in tbl_ln
                if not len(ln.split()) == 1)

    def from_csv():
        return(csv.reader(tbl_ln, skipinitialspace=True))

    tbl_ln = tbl_str.splitlines()
    return { 'pretty': pretty,
             'csv': from_csv }.get(ttype)()


def from_table(table_str, ttype='pretty', key_dir='horizontal'):
    tokens = tokenize(table_str, ttype)
    tbl_list = (table_transpose(tokens) if key_dir == 'vertical'
                else tokens)
    keys = next(tbl_list)
    return [OrderedDict(zip(keys, ln)) for ln in tbl_list]


csv_table = """Col1, Col2, Col3, Numeric Column
Value 1, Value 2, 123, 10.0
Separate, cols, with a tab or 4 spaces, -2,027.1
This is a row with only one cell,,,
"""


pretty_table = """+-------+-------+-------+
| item1 | item2 | item3 |
+-------+-------+-------+
| a1    | a2    | a3    |
| b1    | b2    | b3    |
+-------+-------+-------+
"""

vertical_pt = """+--------+--------+
| key    | value  |
+--------+--------+
| item1  |  asd   |
| item2  |  qwe   |
| item3  |  poi   |
+--------+--------+
"""


def main():
    print (json.dumps(from_table(pretty_table), indent=2))
    print (json.dumps(from_table(vertical_pt, key_dir='vertical')[0],
                      indent=2))
    print (json.dumps(from_table(csv_table, ttype='csv'), indent=2))

if __name__ == '__main__':
        main()
