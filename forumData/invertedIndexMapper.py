#!/usr/bin/python

# Count how many time each word is used on the forum

# Solution from tylucaskelley in Github
import sys
import csv
import string

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    specialChars = '.,!?:;"()<>[]#$=-/'

    trans = string.maketrans(specialChars, ' '*len(specialChars))

    for line in reader:
        if len(line) == 19:
            body = line[4]
            nodeId = line[0]
			body = body.translate(trans)
			words = body.strip().split()
			for word in words:
			    print "{0}\t{1}".format(word.lower(), nodeId)

mapper()
