#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = 0

    for key, val in a_dictionary.items():
        if val > max_val:
            max_val = val
            d_key = key

    return d_key
