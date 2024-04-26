#!/usr/bin/python3
""" 5. Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file,
    using a JSON representation:

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, 'w', encoding=utf8) as f:
        json.dump(my_obj, f)
