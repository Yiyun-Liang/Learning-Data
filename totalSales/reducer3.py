#!/usr/bin/python

# Get the total number of sales and total number of sales value from all stores

import sys

totalNum = 0
totalVal = 0.0

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        # if something went wrong, skip this line
        continue

    store, sale = data

    totalNum += 1
    totalVal += float(sale)


print totalNum, ",", totalVal
