#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx >= len(my_list)) or (idx < 0):
        lcopy = my_list.copy()
        return lcopy
    elif (idx >= 0) and (idx < len(my_list)):
        new_list = my_list.copy()
        new_list[idx] = element
        return(new_list)
    else:
        break
