#!/usr/bin/python3
def no_c(my_string):
    delc = {67: None, 99: None}
    return my_string.translate(delc)
