#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = 0
    d_key = None

    if a_dictionary == None:
        return None

    for key, val in a_dictionary.items():
        if val > max_val:
            max_val = val
            d_key = key

    return d_key
