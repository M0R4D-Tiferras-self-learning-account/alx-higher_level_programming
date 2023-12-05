#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    x = len(my_list) - 1
    for i in range(x, -1, -1):
        print("{}".format(my_list[i]))


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
