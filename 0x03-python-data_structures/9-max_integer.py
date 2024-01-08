#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = 0
    if len(my_list) == 0:
        return(None)

    for element in my_list:
        if max_val < element:
            max_val = element
    return (max_val)
