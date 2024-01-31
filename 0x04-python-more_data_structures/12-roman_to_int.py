#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return None

    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    converted_value = 0

    for letter in roman_string:
        for numeral, numeral_value in roman_numerals.items():
            if letter == numeral:
                if numeral_value > converted_value:
                    converted_value = numeral_value - converted_value
                else:
                    converted_value += numeral_value

    return converted_value
