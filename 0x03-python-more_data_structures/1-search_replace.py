#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    for elem in range(len(my_list)):
        if my_list[elem] == search:
            newlist[elem] = replace
    return newlist
