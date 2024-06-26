#!/usr/bin/python3
""" 6. Create object from a JSON file"""

import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file”:

    Args:
        filename (str): json file
    """
    with open(filename, 'r') as f:
        py_dict = json.load(f)
    return py_dict
