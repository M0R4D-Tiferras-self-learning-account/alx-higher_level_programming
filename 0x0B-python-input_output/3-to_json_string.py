#!/usr/bin/python3
""" 3. To JSON string"""

import json


def to_json_string(my_obj):
    """a function that returns the JSON representation
    of an object (string)

    Args:
        my_obj (string): string to Serialize
    """
    return json.dumps(my_obj)
