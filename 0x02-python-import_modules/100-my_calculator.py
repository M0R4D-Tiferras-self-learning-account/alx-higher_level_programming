#!/usr/bin/python3

import sys

if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
    if len(sys.argv) == 4:
        if sys.argv[2] == "+":
            print(add(int(sys.argv[1]), int(sys.argv[3])))
        elif sys.argv[2] == "-":
            print(sub(int(sys.argv[1]), int(sys.argv[3])))
        elif sys.argv[2] == "*":
            print(mul(int(sys.argv[1]), int(sys.argv[3])))
        elif sys.argv[2] == "/":
            print(div(int(sys.argv[1]), int(sys.argv[3])))
        else:
            print("Unknown operator. Available operators: +, -, * and / ")
            sys.exit("1")
    elif len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit("1")
