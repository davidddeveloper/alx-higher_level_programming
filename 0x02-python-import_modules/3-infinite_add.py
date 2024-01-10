#!/usr/bin/python3
import sys

argv = sys.argv
len_argv = len(argv)

if __name__ == '__main__':
    sum = 0

    for n in range(1, len_argv):
        item = int(argv[n])
        sum += item
    print(sum)
