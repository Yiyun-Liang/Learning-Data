#!/usr/bin/python

# Number of hits made by an ip

import sys

numHits = 0
oldIP= None

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        continue

    thisIP, thisLink = data

    if oldIP and oldIP != thisIP:
        print "{0} : {1}".format(oldIP, numHits)
        numHits = 0

    numHits += 1
    oldIP = thisIP

# Be careful not to forget outputting the last key
if oldIP != None:
    print oldIP, ":", numHits
