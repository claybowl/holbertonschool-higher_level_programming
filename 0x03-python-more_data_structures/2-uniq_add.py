#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqsum = 0
    for elem in set(my_list):
        uniqsum += elem
    return uniqsum
