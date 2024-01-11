#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0

    for numb in sorted(set(my_list)):
        sum += numb

    return sum
