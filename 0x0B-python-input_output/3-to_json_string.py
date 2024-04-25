#!/usr/bin/python3

import json

""" 3. To JSON string"""


def to_json_string(my_obj):
    """a function that returns the JSON representation
    of an object (string)

    Args:
        my_obj (string): string to Serialize
    """
    to_s = my_obj
    if not(type(my_obj) == str):
        to_s = str(my_obj)
    return json.dumps(to_s)
