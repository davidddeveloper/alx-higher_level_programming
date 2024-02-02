#!/usr/bin/python3
"""5-text_indentation.py

This module contains function to print text under some condition

functions it contained:
    text_indentation(text) - print text under some condition

"""


def text_indentation(text):
    """print text and two new line
    if it sees '?' or '.' or ':'

    Args:
        - text: the text to print

    """

    if type(text) != str:
        raise TypeError("text must be a string")

    line_text = ""
    for letter in text:
        line_text += letter
        for item in ["?", ".", ":"]:
            if item == letter:
                print(line_text.strip())
                print()
                line_text = ""
