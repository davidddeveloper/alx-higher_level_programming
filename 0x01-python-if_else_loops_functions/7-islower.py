#!/usr/bin/python3
def islower(c):
    c_code = ord(c)
    for char_code in range(ord('a'), ord('z') + 1):
        if char_code == c_code:
            return True
    else:
        return False
