import fileinput as fi
# import re
# import itertools as it
# import functools as ft
# import string
# import collections
# import math
# import sys

# # findall, search, parse
# from parse import *
# import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(6500)

# Debug logging

# # Input parsing
# INPUT = "".join(fi.input()).rstrip()
# groups = INPUT.split("\n\n")
# lines = list(INPUT.splitlines())

import llist

def solve(n):
    elves = llist.dllist([x+1 for x in range(n)])
    print("Done allocating")

    # idx = 0
    node = elves.first
    while len(elves) > 1:
        if len(elves) % 1000 == 0:
            print(len(elves))
        
        anode = node
        for i in range(len(elves)//2):
            if anode == elves.last:
                anode = elves.first
            else:
                anode = anode.next


        # x = elves.nodeat(len(elves)//2)
        elves.remove(anode)
        if node == elves.last:
            node = elves.first
        else:
            node = node.next

    # print(elves)
    # return elves[(idx-1) % len(elves)]

    return elves[0]



# print(solve(5))
print(solve(3001330))
# print(solve(3001330))
# for i in range(1,100):
    # print("{}: {}".format(i, solve(i)))
