#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list.sort()
    print(my_list[-1])

a = [1, 2, 3, 4, 5]

max_integer(a)