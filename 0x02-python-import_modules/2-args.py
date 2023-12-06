#!/usr/bin/python3

import sys

arg_number = len(sys.argv) - 1
print("{} arguments:".format(arg_number))

for i, arguments in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arguments))
