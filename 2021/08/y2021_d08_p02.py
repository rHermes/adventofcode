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

# Input parsing
INPUT = "".join(fi.input()).rstrip()
groups = INPUT.split("\n\n")
lines = list(INPUT.splitlines())
numbers = [list(map(int, re.findall("-?[0-9]+", line))) for line in lines]

segs_on = {
    "a": set([0, 2, 3, 5, 6, 7, 8, 9]),
    "b": set([0, 4, 5, 6, 8, 9]),
    "c": set([0, 1, 2, 3, 4, 7, 8, 9]),
    "d": set([2, 3, 4, 5, 6, 8, 9]),
    "e": set([0, 2, 6, 8]),
    "f": set([0, 1, 3, 4, 5, 6, 7, 8, 9]),
    "g": set([0, 2, 3, 5, 6, 8, 9])
}

def aro(line, known, pos):
    # print(known, pos)
    a, b = line.split(" | ")
    for word in a.split(" "):
        pairs = {}
        for a, b in it.combinations(pos.items(), 2):
            if len(a[1]) != 2:
                continue
            if a[0] == b[0]:
                continue
            if a[1] == b[1]:
                pairs[(a[0], b[0])] = a[1]
                pairs[(b[0], a[0])] = a[1]

        pos_digits = set(range(10))
        if len(word) == 2:
            pos_digits = set([1])

        if len(word) == 3:
            pos_digits = set([7])

        if len(word) == 4:
            pos_digits = set([4])

        if len(word) == 5:
            pos_digits = set([2, 3, 5])

        if len(word) == 6:
            pos_digits = set([0, 6, 9])

        if len(word) == 7:
            pos_digits = set([8])

        for k, v in known.items():
            pss = segs_on[k]
            if v in word:
                pos_digits &= pss
            else:
                pos_digits -= pss

        # for k, v in pos.items():
        #     pss = segs_on[k]
        #     if not any(z in word for z in v):
        #         print("lel")
        #         print(k, v, word, pss, pos_digits)
        for (a,b), v in pairs.items():
            if v.issubset(word):
                # print("YEA")
                # print(a,b,word,pos_digits)
                # print(pos)
                pos_digits &= (segs_on[a] & segs_on[b])



        assert(len(pos_digits) > 0)
        if len(pos_digits) != 1:
            # print(word, pos_digits)
            continue

        digit = list(pos_digits)[0]
        # print("{} must be digit {}".format(word, digit))

        if digit == 1:
            goods = "cf"
        elif digit == 2:
            goods = "acdeg"
        elif digit == 0:
            goods = "abcefg"
        elif digit == 4:
            goods = "bcdf"
        elif digit == 5:
            goods = "abdfg"
        elif digit == 6:
            goods = "abdefg"
        elif digit == 7:
            goods = "acf"
        elif digit == 8:
            goods = "abcdefg"
        elif digit == 9:
            goods = "abdcfg"
        elif digit == 3:
            goods = "acdfg"
        else:
            raise Exception("PLEASE MEAN: {}".format(digit))

        for g in goods:
            pos[g] &= set(word)

        for y in "abcdefg":
            if y in goods:
                continue
            else:
                pos[y] -= set(word)

        # print("YE:", pos)

    return pos

def solve(lines):
    ans = 0
    for line in lines:
        print(line)
        known = {}
        pos = {a: set("abcdefg") for a in "abcdefg"}
        while len(known) < 7:
            pos = aro(line, known, pos)

            for k, v in pos.items():
                if k in known:
                    continue

                if len(v) != 1:
                    continue

                p = list(v)[0]
                known[k] = p
                break
            else:
                print("WE CAN'T FIX!")
                print(known)
                print(pos)
                return

            for k in pos.keys():
                if k not in known:
                    pos[k].discard(p)


        # print(known)
        snu = ""
        rev_known = {v: k for k, v in known.items()}
        for word in line.split(" | ")[1].split(" "):
            leg = set(range(10))
            for w in word:
                leg &= segs_on[rev_known[w]]

            for w in "abcdefg":
                if w in word:
                    continue
                leg -= segs_on[rev_known[w]]


            assert(len(leg) == 1)
            le = list(leg)[0]
            snu += str(le)

        print(snu)
        ans += int(snu)





    return ans

print(solve(lines))
