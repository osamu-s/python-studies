#!/usr/bin/env python

import json
import csv
import re
from collections import OrderedDict
import itertools

def table_transpose(table_list):
    return (list(ln) for ln in zip(*table_list))


def from_table(table_str, ttype='pretty', key_dir='horizontal'):
    def from_pretty(tbl_ln, 
               horizontal_char='-',
               junction_char='+'):

        # find a frame line, without title
        j = re.escape(junction_char)
        h = re.escape(horizontal_char)
        frm = re.compile('^(' + j + h + '+){2,}' + j + '$')
        tbl_frame = next(itertools.ifilter(lambda x: frm.match(x),
                                           tbl_ln), None)
        if tbl_frame == None:
            raise Error('No frame line in the table')

        # determine slicing positions
        sep_idxs = [ i for i, c in enumerate(tbl_frame)
                     if c == junction_char ]
        slices = [ (s+1, e-1) for s, e in zip([0]+sep_idxs, sep_idxs)[1:] ]

        # tokenize each line
        return ([ln[s:e].strip() for s, e in slices]
                for ln in tbl_ln
                if ln != tbl_frame )

    def from_csv(tbl_ln, delimiter=','):
        return(csv.reader(tbl_ln,
                          delimiter=delimiter,
                          skipinitialspace=True ))

    def tbl_type_error(tbl_ln):
        msg = 'Table Type Error: from_table accepts only pretty or csv.'
        raise TypeError(msg)

    f = { 'pretty': from_pretty,
          'csv': from_csv }.get(ttype, tbl_type_error)
    tokens= f(table_str.splitlines())

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
