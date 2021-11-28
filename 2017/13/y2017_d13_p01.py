import fileinput as fi
import re
import itertools as it
import functools as ft
import string

def solve(S):
    ans = 0
    for d in S.keys():
        r = S[d]
        p = d % ((r-1)*2)
        if p == 0:
            ans += r * d

    return ans

scanners = {}
for line in map(str.rstrip, fi.input()):
    a, b = map(int, line.split(": "))
    scanners[a] = b

print(solve(scanners))
