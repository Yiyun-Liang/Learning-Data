#!/usr/bin/python

import sys
import csv

writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

AKey = None
BKey = None

for line in sys.stdin:
    data = line.strip().split()

    if data[1] == 'A':
		AKey = data[0]
		AData = data[2:]

    elif data[1] == 'B':
		BKey = data[0]
		BData = data[2:]

    if AKey == BKey:
        writer.writerow(BData[:3] + [AKey] + BData[3:] + AData)
