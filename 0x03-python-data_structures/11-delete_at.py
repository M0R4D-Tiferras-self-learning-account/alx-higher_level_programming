#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    n_idx = -1 * (len(my_list) - 1)
    if (idx >= len(my_list)) or (idx < n_idx):
        return my_list
    else:
        new_list = my_list.copy()
        del new_list[idx]
        return new_list
