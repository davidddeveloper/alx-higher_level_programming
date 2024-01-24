#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            self.__size = int(size)
        except Exception:
            raise TypeError("size must be an integer")
        else:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
