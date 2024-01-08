#!/usr/bin/python3
def no_c(my_string):
    list_of_character = []
    list_of_character[:] = my_string  # Save string in a list
    my_string = ""

    # Construct a new string removing the c or C
    for character in list_of_character:
        if character == 'c':
            list_of_character.remove('c')
        if character == 'C':
            list_of_character.remove('C')
    for character in list_of_character:
        my_string += character
    return(my_string)
