#!/usr/bin/python3
from os import lseek


i = 0
while i < 99:
    print("{:02d},".format(i), end=" ")
    i += 1
print(i)
