import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys
import heapq

# findall, search, parse
# from parse import *
import more_itertools as mit
# import z3
# import numpy as np
# import lark
# import regex
# import intervaltree as itree

# print(sys.getrecursionlimit())
sys.setrecursionlimit(6500)

# Debug logging
DEBUG = True
def gprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)




def single_run(lines, regs, i, ins):
    while 0 <= i < len(lines):
        parts = lines[i].split(" ")

        if parts[0] == "snd":
            if parts[1].isalpha():
                val = regs[parts[1]]
            else:
                val = int(parts[1])

            i += 1
            return regs, i, ins, val, True

        elif parts[0] == "set":
            if parts[2].isalpha():
                val = regs[parts[2]]
            else:
                val = int(parts[2])

            regs[parts[1]] = val
            i += 1

        elif parts[0] == "add":
            if parts[2].isalpha():
                val = regs[parts[2]]
            else:
                val = int(parts[2])

            regs[parts[1]] = regs[parts[1]] + val

            i += 1

        elif parts[0] == "mul":
            if parts[2].isalpha():
                val = regs[parts[2]]
            else:
                val = int(parts[2])

            regs[parts[1]] = regs[parts[1]] * val

            i += 1

        elif parts[0] == "mod":
            if parts[2].isalpha():
                val = regs[parts[2]]
            else:
                val = int(parts[2])

            regs[parts[1]] = regs[parts[1]] % val

            i += 1

        elif parts[0] == "rcv":
            if len(ins) == 0:
                return regs, i, ins, None, True
        
            v = ins.pop(0)
            regs[parts[1]] = v

            i += 1
        elif parts[0] == "jgz":
            if parts[1].isalpha():
                a = regs[parts[1]]
            else:
                a = int(parts[1])

            if parts[2].isalpha():
                b = regs[parts[2]]
            else:
                b = int(parts[2])

            if 0 < a:
                i += b
            else:
                i += 1
        else:
            print(parts)
            raise Exception("ERROR")

    return regs, i, ins, None, False

def solve(lines):
    a_regs = collections.defaultdict(int)
    a_regs["p"] = 0
    a_ip = 0
    a_ins = []
    a_running = True
    a_waiting = False

    b_regs = collections.defaultdict(int)
    b_regs["p"] = 1
    b_ip = 0
    b_ins = []
    b_running = True
    b_waiting = False

    ans = 0
    while (a_running or b_running) and not (b_waiting and a_waiting):
        if a_running:
            a_regs, a_ip, a_ins, a_out, a_running = single_run(lines, a_regs, a_ip, a_ins)
            if a_out is not None:
                b_ins.append(a_out)
            else:
                a_waiting = a_running

        if b_running:
            b_regs, b_ip, b_ins, b_out, b_running = single_run(lines, b_regs, b_ip, b_ins)
            if b_out is not None:
                ans += 1
                a_ins.append(b_out)
            else:
                b_waiting = b_running

    return ans
        
# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())

print(solve(lines))
