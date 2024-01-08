#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for element in new_list:
        idx = my_list.index(element)
        if element % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] =  False
    return(new_list)
