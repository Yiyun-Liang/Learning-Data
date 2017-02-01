#!/usr/bin/python

import sys
    for line in sys.stdin:
        data = line.strip().split()

        if len(data) == 10:
            ip, identity, username, ts, tzone, mathod, path, protocol, status, size = data
            print "{0}\t{1}".format(ip, path)


if __name__ == "__main__":
    mapper()
