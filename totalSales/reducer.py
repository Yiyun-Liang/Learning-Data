#!/usr/bin/python

# Hadoop default: only one reducer who gets all the keys
# Reducer receives something like this:

# Miami  12.35
# Miami  68.9
# Miami  32.3
# NYC    67.5
# NYC    0.63

import sys

salesTotal = 0.0
oldKey = None
dummy_Data = ["Miami 12.34","Miami 99.07","Miami 55.07","NYC 88.97","NYC 33.56"]

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        # if something went wrong, skip this line
        continue

    thisKey, thisSale = data

    if oldKey and oldKey != thisKey:
        print "{0} : {1}".format(oldKey, salesTotal)

        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

# Be careful not to forget outputting the last key
if oldKey != None:
    print oldKey, ":", salesTotal
