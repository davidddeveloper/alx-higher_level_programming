#!/usr/bin/python3
def pow(a, b):
    result = 0

    if b == 0:
        result = 1
        return result
    if b < 0:
        a = -a
        result = 1 / (a * a)
        return result
    if a < 0:
        a = -a
        for i in range(b):
            result = a * a
        return result

    for i in range(b):
        result = a * a
    return result
