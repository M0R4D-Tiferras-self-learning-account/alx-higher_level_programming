#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_number = len(sys.argv) - 1
    if arg_number == 0:
        print("0 argument.")
    elif arg_number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_number))
    for i in range(arg_number):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))