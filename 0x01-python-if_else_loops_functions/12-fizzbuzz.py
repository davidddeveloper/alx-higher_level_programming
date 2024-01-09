#!/usr/bin/python3
def fizzbuzz():
    # multiples of three print Fizz instead of the number
    # multiples of five print Buzz
    # multiples of both three and five print FizzBuzz
    for n in range(1, 101):
        if n % 15 == 0:
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")
