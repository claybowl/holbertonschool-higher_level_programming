#!/usr/bin/python3
from itertools import count


if __name__ == "__main__":
    import sys
	numb = len(sys.argv)
    if numb == 1:
        print("{} arguments,".format(numb - 1))
    elif numb == 2:
        print("{} arguments,".format(numb - 1))
    else:
        print("{} arguments,".format(numb - 1))

    for i in range(1, numb):
        print("{}: {}".format(i, sys.argv[i]))
