#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx > len(my_list)) or (idx < 0):
        lcopy = my_list
        return lcopy
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return(new_list)
