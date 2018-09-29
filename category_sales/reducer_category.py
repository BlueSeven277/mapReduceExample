#!/usr/bin/env python

import sys
from sys import exit

current_sale = 0
current_category = None
# word = None
category = None

# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    try:
        category, sales = line.split('\t', 1)
    except ValueError:
        continue

    try:
        sales = float(sales)
    except ValueError:
        continue

    if  current_category == category:
        current_sale += sales
    else:
        if current_category:

                print '%s\t%s' % (current_category, current_sale)
        current_sale = sales
        current_category = category
if current_category == category:
    print '%s\t%s' % (current_category, current_sale)

