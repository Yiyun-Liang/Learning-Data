import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split()

    date, time, store, item, cost, payment = data
        
    if store == "Reno":
        print "{0}\t{1}".format(store, cost)


if __name__ == "__main__":
    mapper()
