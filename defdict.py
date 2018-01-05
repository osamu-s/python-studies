#!/usr/bin/env python3

from collections import defaultdict

def rec_dd():
    return defaultdict(rec_dd)

def main():
    a = defaultdict(dict)
    b = rec_dd()
    b[1][5] = 'mng_OS'

    print (len(b[1]))


if __name__ == '__main__':
    main()
