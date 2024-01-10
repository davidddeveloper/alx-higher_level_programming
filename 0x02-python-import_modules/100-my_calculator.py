#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys


def calculator(a, b, operator):
    """My Calculator Function

    Args:
        a: first integer
        b: second integer

    Returns:
        The value of a operator b
    """
    result = []
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)

    print("{1} {3} {2} = {0}".format(result, a, b, operator))
    exit(0)


argv = sys.argv
argv_len = len(argv)

if argv_len < 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

else:
    operator = argv[2]
    operators = ["+", "-", "*", "/"]
    number_one = int(argv[1])
    number_two = int(argv[3])

    for oper in operators:
        if operator == oper:
            calculator(number_one, number_two, operator)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
