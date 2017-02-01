#!/usr/bin/python

# should print out 10 lines containing longest posts

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    longPosts = []

    for line in reader:

        post = line[4]
        longPosts.append([len(post), line])

    # sort in descending order
    topTen = sorted(longPosts, reverse=True)[0:10]

    # output in ascending order
    topTen = sorted(topTen, reverse=False)

    for top in topTen:
        writer.writerow(top[1])


def alternativeMapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    longPosts = []

    for line in reader:
        longPosts.append(line)

    topTen = sorted(longPosts,key=lambda a: int(a[4]),reverse=False)[-10 if len(longPosts)>10 else -1*len(longPosts):]

    for top in topTen:
        writer.writerow(top)


test = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test)
    alternativeMapper()
    sys.stdin = sys.__stdin__

main()
