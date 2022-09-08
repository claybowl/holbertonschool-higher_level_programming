#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = dict()
    for item in a_dictionary:
        newdict[item] = a_dictionary[item] * 2
    return newdict
