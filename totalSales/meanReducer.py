#!/usr/bin/python

# should do the math for total sales on each day for each store

import sys

salesTotal = 0.0
oldDay = None
count = 0

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        continue

    thisDay, thisSale = data

    if oldDay and oldDay != thisDay:
        print "{0} : {1}".format(oldDay, salesTotal/count)
        salesTotal = 0.0
        count = 0

    oldDay = thisDay
    salesTotal += float(thisSale)
    count += 1

# Be careful not to forget outputting the last key
if oldDay != None:
    print oldDay, ":", (salesTotal/count)
