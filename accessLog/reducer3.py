#!/usr/bin/python

# Most popular file's pathname

import sys

numHits = 0
maxHits = 0
maxLink = None
oldLink = None

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        continue

    ip, thisLink = data

    if oldLink and oldLink != thisLink:
        if numHits > maxHits:
            maxHits = numHits
            maxLink = oldLink

        numHits = 0

    numHits += 1
    oldLink = thisLink

print maxLink, ":", maxHits
