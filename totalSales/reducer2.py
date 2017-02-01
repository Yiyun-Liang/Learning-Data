#!/usr/bin/python

# Getting the highest sale item for each store

import sys

maxSale = 0.0
oldStore = None

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        # if something went wrong, skip this line
        continue

    thisStore, thisSale = data

    if oldStore and oldStore != thisStore:
        print "{0} : {1}".format(oldStore, maxSale)
        maxSale = 0

    if float(thisSale) > maxSale:
        maxSale = float(thisSale)

    oldStore = thisStore

# Be careful not to forget outputting the last key
if oldStore != None:
    print oldStore, ":", maxSale
