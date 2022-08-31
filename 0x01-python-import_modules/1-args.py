#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num = len(sys.argv)
    if num == 1:
        print("{0 arguments.")
    elif num == 2:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(num - 1))
    for i in range(1, num):
        print("{:d}: {:s}".format(i, sys.argv[i]))
