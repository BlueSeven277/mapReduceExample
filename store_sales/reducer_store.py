#!/usr/bin/env python

import sys
from sys import exit

current_sale = 0
current_store = None
# word = None
store = None

# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    try:
        store, sales = line.split('\t', 1)
    except ValueError:
        continue

    try:
        sales = float(sales)
    except ValueError:
        continue

    if  current_store == store:
        current_sale += sales
    else:
        if current_store:

                print '%s\t%s' % (current_store, current_sale)
        current_sale = sales
        current_store = store
if current_store == store:
    print '%s\t%s' % (current_store, current_sale)

