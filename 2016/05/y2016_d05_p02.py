import fileinput as fi
import re
import itertools as it
import functools as ft
import string
import collections
import math
import sys


import hashlib

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

ins = "ugkcyxxp".encode('ascii')
# ins = "abc".encode('ascii')

# for j in range(8):
    # key1 = ins + str(j).encode('ascii')
ans = ['' for _ in range(8)]
added = 0
for i in range(100000000000000000000):
    hsh = hashlib.md5(ins + str(i).encode("ascii")).hexdigest()

    if hsh.startswith("00000"):
        if not hsh[5].isnumeric() or int(hsh[5]) >= 8 or ans[int(hsh[5])] != "":
            print("SKIPPING", hsh[5], hsh[6])
            continue

        print(hsh[5], hsh[6])
        ans[int(hsh[5])] = hsh[6]
        added += 1
        if added == 8:
            break

print("".join(ans))
