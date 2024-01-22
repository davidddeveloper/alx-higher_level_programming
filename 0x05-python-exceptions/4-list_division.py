#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        quotient = 0
        try:
            list_1_item = my_list_1[i]
            list_2_item = my_list_2[i]
            quotient = list_1_item / list_2_item
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(quotient)
    return result
