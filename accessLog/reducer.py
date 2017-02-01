#!/usr/bin/python

# Number of hits on each link

import sys

numHits = 0
oldLink = None

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        continue

    ip, thisLink = data

    if oldLink and oldLink != thisLink:
        print "{0} : {1}".format(oldLink, numHits)
        numHits = 0

    numHits += 1
    oldLink = thisLink

# Be careful not to forget outputting the last key
if oldLink != None:
    print oldLink, ":", numHits
