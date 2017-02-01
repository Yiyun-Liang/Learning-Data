#!/usr/bin/python

# Solution from tylucaskelley in Github

import sys
import csv
import string

count = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split()
	if len(data_mapped) != 2:
		continue

	thisKey, thisValue = data

    # list nodes the word fantastically can be found in
	if thisKey == "fantastically":
		print thisKey, "\t", thisValue

    # print number of times fantastic has appeared
	if oldKey and oldKey != thisKey:
		if oldKey == "fantastic":
			print oldKey, "\t", count
        oldKey = thisKey
        count = 0

	oldKey = thisKey
	count += 1

if oldKey != None:
	print oldKey, "\t", count
