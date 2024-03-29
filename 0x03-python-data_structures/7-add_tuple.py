#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_tup_a = len(tuple_a)
    length_tup_b = len(tuple_b)

    if length_tup_a == 0 and length_tup_b == 0:
        new_tuple = (0, 0)
    elif length_tup_a == 1 and length_tup_b == 1:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif length_tup_a == 1:
        new_tuple = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif length_tup_b == 1:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif length_tup_a == 0:
        new_tuple = (0 + tuple_b[0], 0 + tuple_b[1])
    elif length_tup_b == 0:
        new_tuple = (tuple_a[0] + 0, tuple_a[1] + 0)
    else:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple
