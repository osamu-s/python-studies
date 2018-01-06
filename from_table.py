#!/usr/bin/env python

import json
from collections import OrderedDict

def tokenize(tbl_str, frame=0, sep='+'):
    sep_idxs = [ i for i, c in enumerate(tbl_str[frame])
                 if c == sep ]
    slices = [ (s+1, e-1) for s, e in zip([0]+sep_idxs, sep_idxs)[1:]]
    return ([ln[s:e].strip() for s, e in slices]
            for ln in tbl_str if not len(ln.split()) == 1)


def from_prettytable(table_str):
    tokens = tokenize(table_str.splitlines())
    keys = next(tokens)
    return [OrderedDict(zip(keys, ln)) for ln in tokens]

def from_markdown(table_str):
    tokens = tokenize(table_str.splitlines(), frame=1, sep='|')
    keys = next(tokens)
    return [OrderedDict(zip(keys, ln)) for ln in tokens]

md_table = """|               Col1               |  Col2   |          Col3          | Numeric Column |
|----------------------------------|---------|------------------------|----------------|
| Value 1                          | Value 2 | 123                    |           10.0 |
| Separate                         | cols    | with a tab or 4 spaces |       -2,027.1 |
| This is a row with only one cell |         |                        |                |
"""


pretty_table = """+-------+-------+-------+
| item1 | item2 | item3 |
+-------+-------+-------+
| a1    | a2    | a3    |
| b1    | b2    | b3    |
+-------+-------+-------+
"""

def main():
    print (from_prettytable(pretty_table))
    print (from_markdown(md_table))

if __name__ == '__main__':
        main()
