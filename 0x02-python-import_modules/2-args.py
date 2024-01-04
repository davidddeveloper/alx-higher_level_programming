#!/usr/bin/python3
import sys

argv = sys.argv
len_argv = len(argv) - 1

if __name__ == '__main__':
    print(len_argv, end=" ")
    if len_argv > 1:
        print("arguments:")
    elif len_argv == 0:
        print("arguments.")
    else:
        print("argument:")
    for n in range(1, len_argv + 1):
        print("{}: {}".format(n, argv[n]))
