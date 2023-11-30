#!/usr/bin/python3

for c1 in range(0, 10):
    for c2 in range(c1 + 1, 10):
        if c1 == 8 and c2 == 9:
            print("{}{}".format(c1, c2))
        else:
            print("{}{}".format(c1, c2), end=", ")
