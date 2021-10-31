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

ans = ""
for i in range(100000000000000000000):
    hsh = hashlib.md5(ins + str(i).encode("ascii")).hexdigest()

    if hsh.startswith("00000"):
        print(hsh[5])
        ans += hsh[5]
        if len(ans) == 8:
            break

print(ans)
