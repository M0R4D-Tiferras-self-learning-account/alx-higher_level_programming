#!/usr/bin/python3
""" 3. To JSON string"""

import json


def to_json_string(my_obj):
    """a function that returns the JSON representation
    of an object (string)

    Args:
        my_obj (string): string to Serialize
    """
    if not isinstance(my_obj, str):
        my_obj_s = str(my_obj)
        return json.dumps(my_obj_s)
    return json.dumps(my_obj)
