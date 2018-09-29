#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    data = line.strip().split("\t")
    # test the format of data
    if len(data) == 4:
        store, item, category, cost = data

        # Now print out the data that will be passed to the reducer
        print '%s\t%s' % (category, cost)

