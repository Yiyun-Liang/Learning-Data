#!/usr/bin/python

# Combine forum posts data and user data (join operation in RDBMS)

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
# skip the header in the input file
reader.next()

writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    # forum user from user dataset
    if len(line) == 5:
        writer.writerow([line[0]] + ['A'] + line[1:])

    # forum node from forum posts dataset
    if len(line) == 19:
        writer.writerow([line[3]] + ['B'] + line[:3] + line[5:10])
