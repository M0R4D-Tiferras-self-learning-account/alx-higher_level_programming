#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    sum = 0
    for uniq_num in new_list:
        sum = sum + uniq_num
    return sum
