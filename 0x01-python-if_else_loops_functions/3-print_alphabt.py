#!/usr/bin/python3
alphabet = "".join(
        chr(char_code) for char_code in range(ord('a'), ord('z') + 1)
        if chr(char_code) not in ('q', 'e')
    )
alphabet[4:5]
print("{}".format(alphabet), end='')
