#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return my_list
    else:
        x = len(my_list) - 1
        for i in range(x, -1, -1):
            print("{:d}".format(my_list[i]))
