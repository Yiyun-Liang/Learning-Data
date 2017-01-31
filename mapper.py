#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split()
        
        # have defensive mapper code so that it does not die when it sees error
        # or lines with weird format
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print "{0}\t{1}".format(store, cost)

        #if len(data) == 7:
        #    date, time, store, item1, item2, cost, payment = data
        #    print "{0}{1}\t{2}".format(item1, item2, cost)

if __name__ == "__main__":
    mapper()
