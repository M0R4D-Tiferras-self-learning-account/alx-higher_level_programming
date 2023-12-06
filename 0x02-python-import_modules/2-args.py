#!/usr/bin/python3

if __name__ == "__main__":    
    import sys
    arg_number = len(sys.argv) - 1
    if arg_number == 0:
        print("0 argument.")
    else:
        print("{} arguments:".format(arg_number))
    for i, arguments in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arguments))
