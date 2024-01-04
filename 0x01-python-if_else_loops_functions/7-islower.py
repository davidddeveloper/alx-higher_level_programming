def islower(c):
    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        if c == char:
            return True
        else:
            return False

