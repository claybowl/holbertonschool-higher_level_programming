#!/usr/bin/python3
def numbers(c):
    numb_list = []
    for i in c:
        if i == "M":
            numb_list.append(1000)
        elif i == "D":
            numb_list.append(500)
        elif i == "C":
            numb_list.append(100)
        elif i == "L":
            numb_list.append(50)
        elif i == "X":
            numb_list.append(10)
        elif i == "V":
            numb_list.append(5)
        elif i == "I":
            numb_list.append(1)
        else:
            return None
    return numb_list


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        numb_list = numbers(roman_string)
        res = 0
        current = 0
        if numb_list is not None:
            numb_list.insert(0, 0)
            for x in range(len(numb_list)):
                if x == 0:
                    nextval = numb_list.pop()
                    continue
                if nextval < current:
                    res = res - nextval
                else:
                    res = res + nextval
                current = nextval
                nextval = numb_list.pop()
    return res
