#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length_of_list = len(my_list)
    for idx in range(length_of_list):
        print("{:d}".format(my_list[(length_of_list - 1) - idx]))
