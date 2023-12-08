#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    f_index = len(my_list) - 1
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if (i % 2) == 0:
                new_list.append(True)
            else:
                new_list.append(False)
    return new_list
